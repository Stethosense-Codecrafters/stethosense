# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from pulp import * 
# import seaborn as sns

# data = pd.read_csv('nutrition.csv').drop('Unnamed: 0',axis=1)
# data = data[['name','serving_size','calories','carbohydrate','total_fat','protein']]

# sns.countplot(data.serving_size.map(lambda x: x[:-2]))
# data = data.drop('serving_size',axis=1)


# data['carbohydrate'] = np.array([data['carbohydrate'].tolist()[i].split(' ') for i in range(len(data))])[:,0].astype('float')
# data['protein'] = np.array([data['protein'].tolist()[i].split(' ') for i in range(len(data))])[:,0].astype('float')
# data['total_fat'] = np.array([data['total_fat'].tolist()[i].split('g') for i in range(len(data))])[:,0].astype('float')


# sums = data[['carbohydrate','total_fat','protein']].sum()

# # Create DataFrame for plotting
# plot_data = pd.DataFrame({'Nutritional Values': sums.index, 'Grams (g)': sums.values})

# plt.figure(figsize=(20,10))
# sns.barplot(x='Nutritional Values', y='Grams (g)', data=plot_data)
# plt.grid(alpha=0.2)
# plt.xlabel('Nutritional Values in the dataset',fontsize=18)
# plt.ylabel('Grams (g)',fontsize=18)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)


def build_nutritional_values(kg,calories):
    protein_calories = kg*4
    res_calories = calories-protein_calories
    carb_calories = calories/2.
    fat_calories = calories-carb_calories-protein_calories
    res = {'Protein Calories':protein_calories,'Carbohydrates Calories':carb_calories,'Fat Calories':fat_calories}
    return res

def extract_gram(table):
    protein_grams = table['Protein Calories']/4.
    carbs_grams = table['Carbohydrates Calories']/4.
    fat_grams = table['Fat Calories']/9.
    res = {'Protein Grams':protein_grams, 'Carbohydrates Grams':carbs_grams,'Fat Grams':fat_grams}
    return res

# EXAMPLE
# perfect_proportion = list(extract_gram(build_nutritional_values(70,1500)).values())
# plt.figure(figsize=(20,10))
# sns.barplot(x=list(extract_gram(build_nutritional_values(70,1500)).keys()), y=perfect_proportion)
# plt.grid(alpha=0.2)
# plt.xlabel('Nutritional Values',fontsize=18)
# plt.ylabel('Indicative ideal proportion in your diet (grams)',fontsize=18)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)

# shuffled_data = data.sample(frac=1).reset_index().drop('index',axis=1)
# split_data_loc = np.linspace(0,len(shuffled_data),8).astype(int)
# shuffled_data.loc[split_data_loc[0]:split_data_loc[1]]

week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# split_values = np.linspace(0,len(data),8).astype(int)
# split_values[-1] = split_values[-1]-1
# def random_dataset():
#     frac_data = data.sample(frac=1).reset_index().drop('index',axis=1)
#     day_data = []
#     for s in range(len(split_values)-1):
#         day_data.append(frac_data.loc[split_values[s]:split_values[s+1]])
#     return dict(zip(week_days,day_data))



def calculate_calorie_requirements(gender, age, height_cm, weight_kg):
    # Constants for calorie calculation
    BMR_MALE = 88.362
    BMR_FEMALE = 447.593
    ACTIVITY_MULTIPLIER = 1.375  # Slightly active

    # Determine BMR based on gender
    if gender.lower() in ('m', 'male'): bmr = BMR_MALE
    elif gender.lower() in ('f', 'female'): bmr = BMR_FEMALE
    elif gender.lower() in ('o', 'other'): bmr = (BMR_MALE + BMR_FEMALE)/2
    else: raise ValueError("Invalid gender. Use 'M' for Male or 'F' for Female.")

    # Calculate BMR using the Mifflin-St Jeor equation
    bmr += 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age

    return  bmr * ACTIVITY_MULTIPLIER

# Example usage:
# gender = 'M'  # 'M' for Male or 'F' for Female
# age = 30
# height_cm = 175  # Height in centimeters
# weight_kg = 70  # Weight in kilograms

# calorie_requirements = calculate_calorie_requirements(gender, age, height_cm, weight_kg)
# print(f"Daily calorie requirements: {calorie_requirements} calories")


import pickle


def model(prob,day,kg,calories):
    with open('days_data.pkl', 'rb') as file:
        days_data = pickle.load(file)

    G = extract_gram(build_nutritional_values(kg,calories))
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
    values = np.array(values).round(2).astype(float)
    sol = pd.DataFrame(np.array([food,values]).T, columns = ['Food','Quantity'])
    sol['Quantity'] = sol.Quantity.astype(float)
    sol = sol[sol['Quantity']!=0.0]
    sol.Quantity = sol.Quantity*100
    sol = sol.rename(columns={'Quantity':'Quantity (g)'})
    return sol

def total_model(kg,calories):
    result = []
    for day in week_days:
        prob  = pulp.LpProblem( "Diet", LpMinimize )
        print('Building a model for day %s \n'%(day))
        result.append(model(prob,day,kg,calories))
    return dict(zip(week_days,result))

