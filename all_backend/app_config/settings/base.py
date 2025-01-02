"""
This module contains necessary configurations for Django application setup.
"""

import os
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
SECRET_KEY= os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError('SECRET_KEY environment variable not set!')
DEBUG= False

CSRF_TRUSTED_ORIGINS=[]

ALLOWED_HOSTS= []
INSTALLED_APPS= []
ROOT_URLCONF= 'app_config.urls'
ASGI_APPLICATION= 'app_config.asgi.application'
WSGI_APPLICATION= 'app_config.wsgi.application'

MIDDLEWARE=[
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':os.getenv('POSTGRESQL_DATABASE_NAME'),
        'USER':os.getenv('POSTGRESQL_DATABASE_USER'),
        'PASSWORD':os.getenv('POSTGRESQL_DATABASE_PASSWORD'),
        'HOST':os.getenv('POSTGRESQL_DATABASE_HOST'),
        'PORT':os.getenv('POSTGRESQL_DATABASE_PORT'),
    },
}
connect(
    db=os.getenv('MONGO_DATABASE_NAME'),
    host=os.getenv('MONGO_URI'),
    port= 27017,
)

LANGUAGE_CODE='en-us'
TIMEZONE= 'UTC'
USE_TZ= True
USE_I18N= True  # internationalization
USE_L10N= True  # localization

# Static files to be served using CDN or Nginx from frontend Angular

LOG_DIR= os.path.join(BASE_DIR, 'logs')
INFO_DIR= os.path.join(LOG_DIR, 'info')
ERROR_DIR= os.path.join(LOG_DIR, 'errors')
WARNING_DIR= os.path.join(LOG_DIR, 'warnings')

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(INFO_DIR, exist_ok=True)
os.makedirs(ERROR_DIR, exist_ok=True)
os.makedirs(WARNING_DIR, exist_ok=True)

LOGGING={
    'version':1,
    'disable_existing_handlers':False,
    'handlers':{
        'info_file':{
            'class':'logging.handlers.RotatingFileHandler',
            'level':'INFO',
            'filename':os.path.join(INFO_DIR, 'info.logs'),
            'maxBytes':1024*1024*5,
            'backupCount':5,
        },
        'error_file':{
            'class':'logging.handlers.RotatingFileHandler',
            'level':'ERROR',
            'filename':os.path.join(ERROR_DIR, 'error.logs'),
            'maxBytes':1024*1024*5,
            'backupCount':5,
        },
        'warning_file':{
            'class':'logging.handlers.RotatingFileHandler',
            'level':'WARNING',
            'filename':os.path.join(WARNING_DIR, 'warning.logs'),
            'maxBytes':1024*1024*5,
            'backupCount':5,
        },
        'console_logging':{
            'class':'logging.StreamHandler',
            'level':'ERROR',
        },
    },
    'loggers':{
        'django':{
            'handlers':['info_file', 'error_file', 'warning_file', 'console_logging'],
            'level':'ERROR',
            'propagate':True,
        },
    },
}