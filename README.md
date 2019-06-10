virtualenv env
env\Scripts\activate
pip install django
pip install djangorestframework
pip install django psycopg2
pip install django-cors-headers



----psql
CREATE DATABASE ashnadb;


set your psql username and psql pass in setting.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ashnadb',
        'USER': 'alireza',
        'PASSWORD': '09109840278',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}