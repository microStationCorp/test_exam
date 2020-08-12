from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Topic, Marksheet, Subject
from django.db.models import Count
# Create your views here.


@login_required(login_url='../login')
def timeline(response):
    topics = Topic.objects.all().order_by('-dateOfUpload')[:5]
    data = []
    for t in topics:
        if not Marksheet.objects.filter(user=response.user, topic_id=t.id).exists():
            data.append({
                'topic': t,
                'done': False,
            })
        else:
            data.append({
                'topic': t,
                'done': True,
            })

    if len(Topic.objects.all().order_by('-dateOfUpload')) > 5:
        latest = True
    else:
        latest = False

    s = Subject.objects.annotate(total_set=Count('topic'))

    return render(response, 'timeline/timeline.html', {'data': data, 'latest': latest, 'sub': s})
