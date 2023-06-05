from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils import timezone
from .models import JobPost
from django.core.mail import send_mail,EmailMessage
from Snoffle_tech.settings import EMAIL_HOST_USER
# Create your views here.
def career_page(request):
    jobset = JobPost.objects.filter(last_date__gte=timezone.now())
    if jobset.exists():
        return render(request,'career.html',{'jobset':jobset})
    return render(request,'career.html',{'error':'No job postings available at the moment'})

def jobDetailsPage(request,job_id):
    job = JobPost.objects.filter(id=job_id)[0]
    return render(request,'jobdetails.html',{'job':job})

def job_apply_form(request,job_id):
    sender=EMAIL_HOST_USER
    job = JobPost.objects.filter(id=job_id)[0]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        file = request.FILES.get('file')
        
        mail1 = EmailMessage(
        subject=f'{name} applied for {job.role}',
        body=f"Name: {name}\nEmail: {email}\nPhone: {phone}",
        from_email=sender,
        to=['support@snoffletech.com'],
        )
        mail = EmailMessage(
            subject="In response to your application at Snoffle Technologies",
            body=f'Hello Mr/Mrs {name}\nWe are happy to hear from you.\nWe hope this email finds you well. Thank you for your recent application for the position at Snoffle Technologies. We appreciate your interest in joining our team and taking the time to submit your application.\n\nWe will carefully review your application and respond at the earliest.\nYours Sincerily\nTeam at Snoffle Tech',
            from_email=sender,
            to=[email]
        )
        try:
            mail1.attach(file.name, file.read(),file.content_type)
            # Attach the file to the email message
            mail1.send()
            mail.send()
            return render(request, 'success.html')
        except Exception as e:
            return render(request, 'jobapply.html',{'error':e})
    else:
        return render(request, 'jobapply.html')
