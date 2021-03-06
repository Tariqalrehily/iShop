from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
import os


def emailView(request):
    """
    Create conatct form view 
    Credit to William Vincent
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, [os.environ.get("EMAIL_ADDRESS")])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    messages.error(request, "Success! Thank you for your message, we will get back to you shortly.")
    return redirect(reverse('products'))
