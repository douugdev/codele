from django.urls import path, include
from . import views

urlpatterns = [
    path('questions/', views.questions, name='codele-questions'),
    path('questions/create/', views.create_question, name='codele-create-question'),
    path('questions/<question_id>/', views.question, name='codele-question'),
    path('questions/<question_id>/responder', views.answer, name='codele-create-answer'),
]
