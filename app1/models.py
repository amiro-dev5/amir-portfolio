from django.db import models

# Create your models here.
from django.db import models
#for ma projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    tech_used = models.CharField(max_length=200, help_text="e.q፦ Django, Tailwind, Docker")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Dynamic CV
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, help_text="must be on for it to be seen on the portfolio")

    def __str__(self):
        return f"Resume uploaded on {self.uploaded_at}"

# 3. ma Skills
class Skill(models.Model):
   
    CATEGORY_CHOICES = [
        ('AI', 'Artificial Intelligence & ML'),
        ('BE', 'Backend Development'),
        ('FE', 'Frontend Development'),
        ('DB', 'Database Management'),
        ('LG', 'Languages'),
        ('OT', 'Other Tools'),
    ]
    
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="e.g፦ fab fa-python")
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='BE')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    


class Profile(models.Model):
    image = models.ImageField(upload_to='profile/')
    bio_text = models.TextField(help_text="u can arrange the text abt me")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile updated on {self.updated_at}"

# app1/models.py
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200, help_text="e.q፦ Google, Coursera, Udemy")
    image = models.ImageField(upload_to='certificates/')
    description = models.TextField(blank=True)
    date_received = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"       