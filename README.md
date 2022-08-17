#References
>https://www.bezkoder.com/django-angular-11-crud-rest-framework/#Django_Angular_11_example_Overview

>https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

>https://www.django-rest-framework.org/tutorial/quickstart/


### Open in PyCharm: django-angular-backend-base

### Create a virtual environment to isolate our package dependencies locally
>python3 -m venv <env_name>

>source <env_name>/bin/activate

Deactivate Venv
> deactivate

### Change directory for AppRestApis
> cd AppRestApis

### Install Django and Django REST framework into the virtual environment

Install these if not yet existing
> pip install django

> pip install djangorestframework

Save installed configs on requirements.txt
> pip freeze > requirements.txt

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

Then Install the python library for connecting PostgreSQL
> pip install psycopg2

### [Optional] Use requirements.txt if package is already existing ready for installation
> pip install -r requirements.txt

### Now sync your database for the first time
> python manage.py migrate

### Create an initial user named 'admin' for django rest admin
> python manage.py createsuperuser --email admin@example.com --username admin

### Run server
> python manage.py runserver 8080


## Deploying Django in AWS
> https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

## Install EB CLI
> https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html#eb-cli3-install.scripts

## Adding Database
> https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html
NOTE: Don't forget to add your local IP for the allowed inbound rules ob the RDS DB that you created

### Connecting to AWS RDS using MySQL Workbench
> https://stackoverflow.com/questions/28429493/how-to-connect-mysql-workbench-to-amazon-rds

### AWS root Login Credentials:
> deejayt12@gmail.com / <Check>

### Elastic Bean SSH:
> key pair name:  aws-eb

> passphrase: awsebPP

