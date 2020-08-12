from django.shortcuts import render, redirect
from .models import Topic, Subject
from django.db.models import Count

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('../timeline')
    else:
        topics = Topic.objects.all().order_by('-dateOfUpload')[:5]

        if len(Topic.objects.all().order_by('-dateOfUpload')) > 5:
            rest = True
        else:
            rest = False

        s = Subject.objects.annotate(total_set=Count('topic'))
        return render(request, 'home/home.html', {'topics': topics, 'rest': rest, 'sub': s})
