"""
ASGI config for blog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

DEBUG = os.getenv('DEBUG', 'True') == 'True'

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.production')

application = get_asgi_application()
