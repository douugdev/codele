from django.urls import path, include
from . import blog_views, questions_views

urlpatterns = [
    path('api/blog/posts', blog_views.PostsList.as_view()),
    path('api/blog/post/<int:id>', blog_views.PostDetail.as_view()),
    path('api/questions', questions_views.QuestionsList.as_view())
]
