from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from .models import Contact
from django.contrib import messages
import smtplib
# Create your views here.
def index(request):
    return render(request ,'home/index.html')

def base(request):
    return render(request ,'home/base.html')

def pricing(request):
    return render(request ,'home/pricing.html')

def testimonial(request):
    return render(request ,'home/testimonial.html')

def aboutme(request):
    return render(request ,'home/about.html')


def contactme(request):

    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('phone')
        desc=request.POST.get('message')
        name=request.POST.get('name')
        contact=Contact(name=name,email=email,phone=contact,decs=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Authentication
        s.login("editingtricxps@gmail.com", "qwertyuiop@0987654321")

        subject = "Thank you for filling Contact form"
        body= "Hello Prajwal Sapaliya is here Thank you for filling contact form I will response your query within 8 hours"
        # message to be sent
        message = "Subject : {}\n\n{}".format(subject,body)
   
        # sending the mail
        s.sendmail("editingtricxps@gmail.com", email, message)
  
        # terminating the session
        s.quit()
        

    return render(request ,'home/contact.html')
