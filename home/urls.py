from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='codele-home'),
    #path('home',views.home,name='codele-home'),
    path('about',views.about,name='codele-about')
]
