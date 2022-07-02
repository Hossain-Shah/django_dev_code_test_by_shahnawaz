Django Interview Assignment
Tools and Frameworks
Development Environment:

    Python 3.9.5
    Django 4.0.5

Project Setup for Development

    Install Python 3 if not already installed
        Download Python 3 for Windows from https://www.python.org/downloads/
        Extract the .exe file
        Run the .exe file
        Open a command prompt and type python

        sudo apt-get install python

    Clone The Interview Assignment

        git clone https://github.com/Hossain-Shah/django_dev_code_test_by_shahnawaz.git

    Install the requirements using the command:

        pip install -r requirements.txt

    Run the development server using the command

      python manage.py runserver

    To create super user run the command

      python manage.py createsuperuser

    To migrate database run the command

      python manage.py makemigrations
      python manage.py migrate