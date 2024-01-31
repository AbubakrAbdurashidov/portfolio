from django.shortcuts import render, redirect
from django.contrib import messages
from article.models import Article
from .models import (
    Home,
    Subject,
    About,
    Partner,
    TopSkill,
    Skill,
    Education,
    Experience,
    Award,
    Service,
    Project,
    Counter,
)
from .forms import ContactForm


def index(request):
    home = Home.objects.order_by('-id')[:1]
    articles = Article.objects.order_by('-id')[:3]
    education = Education.objects.all()
    experience = Experience.objects.all()
    award = Award.objects.all()
    counter = Counter.objects.all()
    service = Service.objects.order_by('-id')[:6]
    projects = Project.objects.order_by('-id')[:6]
    top_skill = TopSkill.objects.order_by('-id')[:3]
    skills = Skill.objects.order_by('-id')[:6]
    subject = Subject.objects.all()
    # arr = "["
    # for sub in subject:
    #     arr.append(f"""""")
    form = ContactForm()
    about = About.objects.order_by('-id')[:1]
    partners = Partner.objects.order_by('-id')[:5]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('.#navbar_section')
    ctx = {
        'home': home,
        'education': education,
        'articles': articles,
        'experience': experience,
        'award': award,
        'form': form,
        'service': service,
        'counter': counter,
        'projects': projects,
        'top_skill': top_skill,
        'skills': skills,
        'subject': subject,
        'about': about,
        'partners': partners
    }

    return render(request, 'main/index.html', ctx)


def footer(request):
    services = Service.objects.order_by('-id')[:5]

    ctx = {
        'services': services
    }
    return render(request, 'footer.html', ctx)
