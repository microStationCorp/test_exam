from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypfl, name="my profile"),
]
