from django.shortcuts import render
from home.models import Subject, Topic, Marksheet
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='../login')
def subject(request, sub_id):
    topics = Topic.objects.filter(
        subject__id=sub_id).order_by('-dateOfUpload')
    data = []

    if len(topics) == 0:
        has_set = False
    else:
        has_set = True

    for t in topics:
        if Marksheet.objects.filter(user__id=request.user.id, topic_id=t.id).exists():
            data.append({
                'topic': t,
                'done': True
            })
        else:
            data.append({
                'topic': t,
                'done': False
            })

    return render(request, 'subject/subpage.html', {'data': data, 'has_set': has_set, 's_name': Subject.objects.get(id=sub_id).name})
