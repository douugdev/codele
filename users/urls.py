from django.urls import path
from . import views

urlpatterns = [
    path('success/', views.account_created, name='codele-registration-success'),
]
