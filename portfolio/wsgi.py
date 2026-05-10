"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

import os
from django.contrib.auth import get_user_model


User = get_user_model()
if not User.objects.filter(username='amir_admin').exists():
    User.objects.create_superuser('amir_admin', 'amir@example.com', 'Amir@2026_Postgres')
    print("Superuser 'amir_admin' created successfully!")
