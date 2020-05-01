from django.shortcuts import render
from .models import Topic

# Create your views here.


def home(request):
    topics = Topic.objects.all().order_by('-dateOfUpload')
    return render(request, 'home/home.html', {'topics': topics})
