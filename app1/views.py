from django.shortcuts import render
from .models import Project, Resume, Skill,Profile,Certificate
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Portfolio Message from {name}"
        full_message = f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                subject,
                full_message,
                'crpor1487@gmail.com', 
                ['crpor1487@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Something went wrong. Please try again.")
        
        return redirect('/#contact') # 
   
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