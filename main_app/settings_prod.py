
from .settings_base import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['your-home-finance-api.herokuapp.com', 'JhonIdrovo.pythonanywhere.com.']


# STATICFILES_DIRS =[BASE_DIR/'react/dist', 
# '/var/www/static/',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv('NAME')),
        'USER': str(os.getenv('USER')),
        'PASSWORD': str(os.getenv('PASSWORD')),
        'HOST': str(os.getenv('HOST')),
        'TEST': {
          'NAME': str(os.getenv('TEST'))}
    }
}

CORS_ALLOWED_ORIGINS = [
    "https://your-home-finance.herokuapp.com"
]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


#SECURE_HSTS_SECONDS
