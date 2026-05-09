from django.contrib import admin

# Register your models here.
from .models import Project, Resume, Skill,Profile,Certificate
admin.site.register(Project)
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Certificate)