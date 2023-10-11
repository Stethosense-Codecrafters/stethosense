import numpy
import pandas 
from pulp import *
import pickle

class Diet:
    def calculate_calorie_requirements(self, gender, age, height_cm, weight_kg):
        # Constants for calorie calculation
        BMR_MALE = 88.362
        BMR_FEMALE = 447.593
        ACTIVITY_MULTIPLIER = 1.375  # Slightly active

        # Determine BMR based on gender
        if gender.lower() in ('m', 'male'): bmr = BMR_MALE
        elif gender.lower() in ('f', 'female'): bmr = BMR_FEMALE
        elif gender.lower() in ('o', 'other'): bmr = (BMR_MALE + BMR_FEMALE)/2
        else: raise ValueError("Invalid gender. Use 'M'/'Male' for Male, 'F'/'Female' for Female or 'O'/'Other' for Other.")

        # Calculate BMR using the Mifflin-St Jeor equation
        bmr += 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age

        return  bmr * ACTIVITY_MULTIPLIER

    def __init__(self, height, weight, gender, age):
        self.height = float(height)
        self.weight = float(weight)
        self.gender = str(gender)
        self.age = int(age)
        self.calories = self.calculate_calorie_requirements(self.gender, self.age, self.height, self.weight)
        
    def build_nutritional_values(self):
        protein_calories = self.weight*4
        # res_calories = calories-protein_calories
        carb_calories = self.calories / 2.
        fat_calories = self.calories - carb_calories - protein_calories
        return {
            'Protein Calories': protein_calories, 
            'Carbohydrates Calories': carb_calories, 
            'Fat Calories': fat_calories
        }

    def extract_gram(self, table):
        protein_grams = table['Protein Calories']/4.
        carbs_grams = table['Carbohydrates Calories']/4.
        fat_grams = table['Fat Calories']/9.
        res = {'Protein Grams':protein_grams, 'Carbohydrates Grams':carbs_grams,'Fat Grams':fat_grams}
        return res
    
    def model(self, prob, day):
        with open('./static/days_data.pkl', 'rb') as file:
            days_data = pickle.load(file)

        G = self.extract_gram(self.build_nutritional_values())
        E = G['Carbohydrates Grams']
        F = G['Fat Grams']
        P = G['Protein Grams']
        day_data = days_data[day]
        day_data = day_data[day_data.calories!=0]
        food = day_data.name.tolist()
        c  = day_data.calories.tolist()
        x  = pulp.LpVariable.dicts( "x", indices = food, lowBound=0, upBound=1.5, cat='Continuous', indexStart=[] )
        e = day_data.carbohydrate.tolist()
        f = day_data.total_fat.tolist()
        p = day_data.protein.tolist()
        prob  = pulp.LpProblem( "Diet", LpMinimize )
        prob += pulp.lpSum( [x[food[i]]*c[i] for i in range(len(food))]  )
        prob += pulp.lpSum( [x[food[i]]*e[i] for i in range(len(x)) ] )>=E
        prob += pulp.lpSum( [x[food[i]]*f[i] for i in range(len(x)) ] )>=F
        prob += pulp.lpSum( [x[food[i]]*p[i] for i in range(len(x)) ] )>=P
        prob.solve()
        variables = []
        values = []
        for v in prob.variables():
            variable = v.name
            value = v.varValue
            variables.append(variable)
            values.append(value)
        values = numpy.array(values).round(2).astype(float)
        sol = pandas.DataFrame(numpy.array([food,values]).T, columns = ['Food','Quantity'])
        sol['Quantity'] = sol.Quantity.astype(float)
        sol = sol[sol['Quantity']!=0.0]
        sol.Quantity = sol.Quantity*100
        sol = sol.rename(columns={'Quantity':'Quantity (g)'})
        return sol

    def get_diet_plan(self):
        WEEK_DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        result = []
        for day in WEEK_DAYS:
            prob  = pulp.LpProblem( "Diet", LpMinimize )
            print('Building a model for day %s \n'%(day))
            result.append(self.model(prob, day))
        return dict(zip(WEEK_DAYS, result))

    def get_health_profile(self):
        return {
            'Age': self.age,
            'Weight': self.weight,
            'Height': self.height,
            'Gender': self.gender,
            'Calorie Requirement': round(100 * self.calories) / 100
        }
    