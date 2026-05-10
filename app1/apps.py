from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        post_migrate.connect(create_admin_once, sender=self)

def create_admin_once(sender, **kwargs):
    from django.contrib.auth.models import User
    try:
        if not User.objects.filter(username='amir').exists():
            User.objects.create_superuser('amir', 'aad392001@gmail.com', 'Amir@2026')
            print("Admin created successfully!")
    except Exception:
        pass