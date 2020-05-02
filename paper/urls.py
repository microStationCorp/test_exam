from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:topic_id>/', views.qPaper, name='paper'),
    path('paper_submit/<int:topic_id>/', views.pSubmit, name="submit"),
]
