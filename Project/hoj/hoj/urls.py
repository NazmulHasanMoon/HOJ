"""hoj URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path, include
from user import views as user_views
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('standings/', user_views.standings, name='standings'),
    path('profile/', user_views.profile, name='profile'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('problem.urls')),  # problem urls file added 
    path('', include('submission.urls')), # submission urls file added
    path('', include('resources.urls')), # resources urls file added  

    

    

        
]
