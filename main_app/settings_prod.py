
from .settings_base import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['backend-1-410a8b404e22.herokuapp.com']


# STATICFILES_DIRS =[BASE_DIR/'react/dist', 
# '/var/www/static/',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "znixzuonigw7gvo1",
        'USER': str(os.getenv('USER')),
        'PASSWORD': str(os.getenv('PASSWORD')),
        'HOST': str(os.getenv('HOST')),
        'PORT': '3306',
        'OPTIONS':{'isolation_level':None}
    }
}

CORS_ALLOWED_ORIGINS = [
    "https://expenses-manager-2-62216a16a8cf.herokuapp.com"
]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


#SECURE_HSTS_SECONDS
