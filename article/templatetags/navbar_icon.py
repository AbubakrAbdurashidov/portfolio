from django import template

from main.models import Home, Service

register = template.Library()


@register.simple_tag
def navbar_icon():
    return Home.objects.order_by('-id')[0]


@register.simple_tag
def footer_services():
    return Service.objects.order_by('-id')[:5]
