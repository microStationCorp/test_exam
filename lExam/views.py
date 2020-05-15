from django.shortcuts import render
from home.models import Topic, Marksheet
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='../login')
def latest(request):
    topics = Topic.objects.all().order_by('-dateOfUpload')[:50]
    data = []
    for t in topics:
        if not Marksheet.objects.filter(user=request.user, topic_id=t.id).exists():
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
