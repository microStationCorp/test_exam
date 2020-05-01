from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Topic
# Create your views here.


@login_required(login_url='../login')
def timeline(response):
    topics = Topic.objects.all().order_by('-dateOfUpload')
    return render(response, 'timeline/timeline.html', {'topics': topics})
