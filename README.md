#References
>https://www.bezkoder.com/django-angular-11-crud-rest-framework/#Django_Angular_11_example_Overview

>https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

>https://www.django-rest-framework.org/tutorial/quickstart/


### Open in PyCharm: django-angular

### Create a virtual environment to isolate our package dependencies locally
>python3 -m venv <env_name>

>source <env_name>/bin/activate

Deactivate Venv
> deactivate

### Install Django and Django REST framework into the virtual environment
> pip freeze > requirements.txt

> pip install django

> pip install djangorestframework

### If you are using mongodb
> pip install djongo 

### If you are using MySQL
Install first MySQL server and MySQL Workbench
> https://downloads.mysql.com/archives/workbench/

> https://medium.com/@tharunm6/how-to-install-mysql-8-on-macos-catalina-d4cbf39171a6

> https://manjaro.site/step-by-step-installing-mysql-server-on-macos-catalina-10-15-5/

> pip install pymysql

### If you are using POSTGRESQL
Install first PGAdmin for PostGreSQL
> https://www.postgresql.org/ftp/pgadmin/pgadmin4/v5.5/macos/

Than Install the python library for connecting PostgreSQL
> pip install psycopg2

### [Optional] Use requirements.txt if package is already existing ready for installation
> pip install -r requirements.txt

### Now sync your database for the first time
> python manage.py migrate


### Create an initial user named 'admin'
> python manage.py createsuperuser --email admin@example.com --username admin

### Run server
> python manage.py runserver


