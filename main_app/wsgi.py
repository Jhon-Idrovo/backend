"""
WSGI config for main_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE','main_app.settings_local' if os.environ.get('IS_DEV')=='TRUE' else 'main_app.settings_prod')
application = get_wsgi_application()
