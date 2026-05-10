from django.shortcuts import render
from .models import Project, Resume, Skill,Profile,Certificate,ContactMessage
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
           
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Thank you! Your message has been received successfully.")
        except Exception:
            
            messages.error(request, "We encountered an issue saving your message. Please try again later.")
        
        return redirect('/#contact')
   
    projects = Project.objects.all().order_by('-created_at')
    all_skills = Skill.objects.all()
    
    
    skills_by_category = {}
    for cat_code, cat_name in Skill.CATEGORY_CHOICES:
        skills_by_category[cat_name] = all_skills.filter(category=cat_code)
    
    resume = Resume.objects.filter(is_active=True).last()
    profile = Profile.objects.last()
    certificates = Certificate.objects.all().order_by('-id')
    context = {
        'projects': projects,
        'skills_by_category': skills_by_category,
        'resume': resume,
        'profile': profile,
        'certificates': certificates,
    }
    return render(request, 'index.html', context)