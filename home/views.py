from django.shortcuts import render, redirect
from .models import Topic

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('../timeline')
    else:
        topics = Topic.objects.all().order_by('-dateOfUpload')
        return render(request, 'home/home.html', {'topics': topics})
