from django.shortcuts import render
from home.models import Topic, Marksheet

# Create your views here.


def latest(request):
    topics = Topic.objects.all().order_by('-dateOfUpload')[:50]
    data = []
    for t in topics:
        if len(Marksheet.objects.filter(user=request.user, topic_id=t.id)) == 0:
            data.append({
                'topic': t,
                'done': False,
            })
        else:
            data.append({
                'topic': t,
                'done': True,
            })
    return render(request, 'lExam/latest.html', {'data': data})
