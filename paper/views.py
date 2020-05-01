from django.shortcuts import render
from home.models import Questions

# Create your views here.


def qPaper(request, topic_id):
    que = Questions.objects.filter(topic__id=topic_id)
    return render(request, 'paper/paper.html', {'que': que})
