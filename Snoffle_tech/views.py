from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
def home_page(request):
    return render(request,'index.html')

def service_page(request):
    return render(request,'service.html')
def about_page(request):
    return render(request,'about.html')

def email_page(request):
    sender=EMAIL_HOST_USER
    if request.method == 'POST':
        name = request.POST['fullname']
        number = request.POST['mobile_number']
        email = request.POST['email']
        comment = request.POST['comment']
        select = request.POST['select']
        if select=="0":
            return render(request, 'contact.html', {'error_message': 'choose valid option from drop down menu'})
        elif select=='1':
            select='Job'
        elif select=='2':
            select='Internship'
        elif select=='3':
            select='Services'
        sub1 ="In response to your query about Snoffle Technologies"
        message1=f'Hello Mr/Mrs {name}\nWe are happy to hear from you.\nWe will try to get back to you about your query as soon as possible.\nYours Sincerily\nTeam at Snoffle Tech'
        sub2=f'{select}'
        message2=f'Mr/Mrs {name} with the following details\n\nemail: {email}\nnumber: {number}\nwish to enquire about the query:\n{comment}'
            
        try:
            send_mail(subject=sub1,message=message1,from_email=sender,recipient_list=[email])
            send_mail(subject=sub2,message=message2,from_email=sender,recipient_list=['support@snoffletech.com'])
            return redirect('/')
        except Exception as e:
            print(e)
            return render(request, 'contact.html', {'error_message': e})
        
    
    return render(request, 'contact.html')