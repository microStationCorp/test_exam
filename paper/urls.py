from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:topic_id>/', views.qPaper, name='paper'),
    path('description/<int:topic_id>/', views.pDesc, name='description'),
    path('paper_submit/<int:topic_id>/', views.pSubmit, name="submit"),
    path('paper_res/<int:topic_id>/', views.pResult, name="result"),
]
