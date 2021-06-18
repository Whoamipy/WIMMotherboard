from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_drjxtmx_#_xryr^k0#@av+6gh*yhsqo418j*$c2c*#idjzzpo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# - Application Definition
DJANGO_APPS = [
    'django.contrib.admin'       ,
    'django.contrib.auth'        ,
    'django.contrib.contenttypes',
    'django.contrib.sessions'    ,
    'django.contrib.messages'    ,
    'django.contrib.staticfiles' ,
]

LOCAL_APPS = []

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
# - 

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : get_secret('DB_NAME')                   ,
        'USER'      : get_secret('USER')                      ,
        'PASSWORD'  : get_secret('PASSWORD')                  ,
        'HOST'      : get_secret('HOST')                      ,
        'PORT'      : get_secret('PORT')                      ,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL       = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static'),]

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'