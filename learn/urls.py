from django.urls import path, include
from . import views

urlpatterns = [
    path('aprender/', views.welcome, name='codele-welcome'),
    path('aprender/<language>/', views.learn, name='codele-learn'),
    path('aprender/<language>/<lesson_id>', views.lesson, name='codele-lesson'),
]
