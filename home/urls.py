from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='codele-home'),
    path('help',views.view_help,name='codele-help')
]
