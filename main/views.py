from django.shortcuts import render
from .models import (
    Home,
    Subject,
    About,
    Partners,
)


def index(request):
    home = Home.objects.order_by('-id')[:1]
    subject = Subject.objects.all()
    about = About.objects.order_by('-id')[:1]
    partners = Partners.objects.order_by('-id')[:5]
    ctx = {
        'home': home,
        'subject': subject,
        'about': about,
        'partners': partners
    }

    return render(request, 'main/index.html', ctx)


