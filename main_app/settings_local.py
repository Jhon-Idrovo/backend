from .settings_base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']
STATICFILES_DIRS =[BASE_DIR/'react/dist']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://0.0.0.0:8000",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hfdb',
	    'USER': 'postgres',
        'PASSWORD': 'adadfljadf',
        'HOST': 'db',
        'PORT': '5432',
    }
}