from django.shortcuts import render

# Create your views here.
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        # print(subject)
        # print(email)
        # print(message)

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],

        )

    return render(request, 'contact/contact.html', {'myinfo': myinfo})
