from django.urls import path, include
from . import views

urlpatterns = [
    path('duvidas/', views.questions, name='codele-questions'),
    path('duvidas/criar/', views.create_question, name='codele-create-question'),
    path('duvida/<question_id>/', views.question, name='codele-question'),
    path('duvida/<question_id>/responder', views.answer, name='codele-create-answer'),
]
