from django.urls import path, include
from . import views

urlpatterns = [
    path('duvidas/', views.questions, name='codele-questions'),
    path('duvida/<question_id>/', views.question, name='codele-question'),
]
