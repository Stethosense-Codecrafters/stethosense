# Stethosense Installation Guide

Welcome to the Stethosense installation guide. In this document, you'll find step-by-step instructions on how to set up the Stethosense project on your local development environment.

## Prerequisites

Before you begin the installation, make sure you have the following prerequisites installed on your system:

- **Python:** Stethosense is built using Python, so you'll need to have Python 3.6 or higher installed. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

- **Pip:** Pip is the package manager for Python. It's usually installed along with Python. You can check if you have Pip installed by running `pip --version` in your terminal.

- **Virtual Environment (Optional but recommended):** It's a good practice to create a virtual environment for your Python projects. You can create one using `virtualenv` or `venv`. Here's how to install `virtualenv`:

    ```bash
    pip install virtualenv
    ```

## Installation Steps

Follow these steps to set up Stethosense on your local machine:

### Clone the Repository:

If you have Git installed, open your terminal and navigate to the directory where you want to clone the Stethosense repository.

Run the following command to clone the repository:

```bash
git clone https://github.com/aioont/stethosense.git
```

Create a Virtual Environment (Optional but recommended):

Navigate to the project directory:

```cd stethosense```


Create a virtual environment:

```virtualenv venv```

Activate the virtual environment:

On Windows:

bash

```venv\Scripts\activate```

On macOS and Linux:

bash

```source venv/bin/activate```

Install Dependencies:

While in the virtual environment, install the project dependencies using pip:

```bash

pip install -r requirements.txt```

Apply Database Migrations:

Run the following commands to apply database migrations:

```bash

python manage.py makemigrations
python manage.py migrate
```
Create a Superuser (Admin User):

Create a superuser account to access the Django admin panel:

```bash

python manage.py createsuperuser
```

Start the Development Server:

Run the following command to start the development server:

```bash

python manage.py runserver
```

Access Stethosense:

Open your web browser and navigate to http://127.0.0.1:8000/ to access the Stethosense application.
Access the Admin Panel:

To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created earlier.



















