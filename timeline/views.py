from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Topic, Marksheet
# Create your views here.


@login_required(login_url='../login')
def timeline(response):
    topics = Topic.objects.all().order_by('-dateOfUpload')
    data = []
    for t in topics:
        if len(Marksheet.objects.filter(user=response.user, topic_id=t.id)) == 0:
            data.append({
                'topic': t,
                'done': False,
            })
        else:
            data.append({
                'topic': t,
                'done': True,
            })

    return render(response, 'timeline/timeline.html', {'data': data})
