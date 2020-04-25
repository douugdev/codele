from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='codele-home'),
    path('about',views.home,name='codele-about')
]
