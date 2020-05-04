from django import template
from django.contrib.auth.models import User
register = template.Library()

@register.filter
def badge(indexable):
    return User.objects.filter(username=indexable).first().profile.badge

@register.filter
def author(indexable):
    return User.objects.filter(username=indexable).first().username

@register.filter
def profile_pic(indexable):
    return User.objects.filter(username=indexable).first().profile.image.url
