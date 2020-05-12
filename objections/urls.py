from django.urls import path
from . import views

urlpatterns = [
    path('', views.objection, name="objections"),
    path('send/', views.sendObj, name="send"),
]
