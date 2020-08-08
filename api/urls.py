from django.urls import path, include
from . import views

urlpatterns = [
    path('api/blog/posts', views.PostsList.as_view()),
    path('api/blog/post/<int:id>', views.PostDetail.as_view())
]
