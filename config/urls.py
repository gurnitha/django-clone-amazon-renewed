"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

# Import views from app/main
from app.main.views import homePage, aboutPage

# Import views from app/adboard
from app.adboard.views import adboardHomePage

urlpatterns = [
    
    # PATHS FOR FRONTEND
    path('', homePage, name='home_page'),
    path('about/', aboutPage, name='about_page'),
    
    # PATHS FOR ADBOARD
    # path('admin/', admin.site.urls),
    path('admin/home', adboardHomePage, name='home_page_adboard')
]
