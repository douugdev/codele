from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='codele-home'),
    path('contact',views.contact,name='codele-contact')
]
