from django.urls import path
from . import views

urlpatterns = [
    path('<int:sub_id>', views.subject, name="subject")
]
