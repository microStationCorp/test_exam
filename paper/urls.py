from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:topic_id>/', views.qPaper, name='paper')
]
