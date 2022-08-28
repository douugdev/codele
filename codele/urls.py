"""codele URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from .admin import admin_site
from django.urls import path, include
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from . import robots

urlpatterns = [
    path('admin/', admin_site.urls),
    path('robots.txt', robots.robots_txt),
    path('profile/', user_views.my_profile, name='codele-profile-w'),
    path('profile/<username>/', user_views.profile, name='codele-profile'),
    path('register/', user_views.register, name='codele-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='codele-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='codele-logout'),
    path('', include('home.urls')),
    path('', include('questions.urls')),
    path('', include('users.urls')),
    path('', include('blog.urls')),
    path('', include('learn.urls')),
    path('', include('api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
