from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.contrib.auth.models import User

def create_admin_once():
    if not User.objects.filter(username='amir').exists():
        User.objects.create_superuser('amir', 'aad392001@gmail.com', 'Amir@2026')
        print("Admin created successfully!")

create_admin_once()