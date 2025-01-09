"""
WSGI config for ecommerce_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


settings_module = 'ecommerce_api.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'ecommerce_api.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',settings_module )
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_api.settings')

application = get_wsgi_application()
