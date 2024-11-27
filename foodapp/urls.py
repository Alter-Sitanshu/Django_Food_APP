"""
URL configuration for foodapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from login.views import login_view,registration_view, logout_view, profile_view, profile_creation

# for serving the stsatic files uploaded by the user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', include('landing.urls')),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profilecreation/', profile_creation, name='create_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This is for serving user static files
