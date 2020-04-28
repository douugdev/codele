from django.urls import path, include
from . import views

urlpatterns = [
path('success/', views.account_created, name='codele-registration-sucess'),
]
