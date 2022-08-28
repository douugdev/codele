from django.urls import path, include
from . import views

urlpatterns = [
    path('learn/', views.welcome, name='codele-welcome'),
    path('learn/<language>/', views.learn, name='codele-learn'),
    path('learn/<language>/<lesson_id>', views.lesson, name='codele-lesson'),
]
