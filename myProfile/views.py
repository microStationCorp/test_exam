from django.shortcuts import render, redirect
from home.models import Topic, Marksheet
from django.conf import settings

# Create your views here.


def mypfl(request):
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, f"/myprofile"))
    else:
        ms = Marksheet.objects.filter(user=request.user)
        top = []
        for m in ms:
            top.append({
                'name': Topic.objects.get(id=m.topic_id).topic_name,
                'perc': m.percentage,
                'rank': list(Marksheet.objects.filter(topic_id=m.topic_id).order_by("-percentage").values_list('user__id', flat=True)).index(request.user.id)+1,
                'total': len(Marksheet.objects.filter(topic_id=m.topic_id)),
                'topper': Marksheet.objects.filter(topic_id=m.topic_id).order_by("-percentage").first().user.username,
                'tper': Marksheet.objects.filter(topic_id=m.topic_id).order_by("-percentage").first().percentage
            })

        context = {
            "top": top
        }

        return render(request, 'myProfile/profile.html', context)
