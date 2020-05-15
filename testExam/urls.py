"""testExam URL Configuration

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
from django.urls import path, include
from home import views
from . import views as views_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('timeline/', include('timeline.urls')),
    path('paper/', include('paper.urls')),
    path('logout/', views_logout.myLogout, name='logout'),
    path('myprofile/', include('myProfile.urls')),
    path('latest/', include('lExam.urls')),
    path('objections/', include('objections.urls')),
    path('subject/', include('subject.urls'))
]
