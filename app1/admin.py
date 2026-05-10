from django.contrib import admin

# Register your models here.
from .models import Project, Resume, Skill,Profile,Certificate,ContactMessage
admin.site.register(Project)
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Certificate)

#for the message
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
   # (Columns)
    list_display = ('name', 'email', 'created_at')
    
    search_fields = ('name', 'email')
    
    list_filter = ('created_at',)
    
    readonly_fields = ('name', 'email', 'message', 'created_at')