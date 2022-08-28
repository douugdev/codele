from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='codele-blog'),
    path('blog/<post_id>', views.post, name='codele-post')
]
