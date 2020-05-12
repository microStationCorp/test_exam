from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from home.models import Objection, Reply, Questions

# Create your views here.


@login_required(login_url='../login')
def objection(request):
    obj = Objection.objects.filter(
        user_id=request.user.id).order_by("-dateOfReport")[:30]

    data = []

    for o in obj:
        if Reply.objects.get(ques_id=o.ques_id).reply == '':
            reply = None
        else:
            reply = Reply.objects.get(ques_id=o.ques_id).reply

        data.append({
            "ques_id": o.ques_id,
            'ques': Questions.objects.get(id=o.ques_id),
            'reply': reply
        })

    return render(request, 'objections/obj.html', {'data': data})


def sendObj(request):
    if request.is_ajax() and request.method == "GET":

        try:
            Objection.objects.get(user_id=request.user.id,
                                  ques_id=request.GET['ques_id'])
        except:
            obj = Objection(user_id=request.user.id,
                            ques_id=request.GET['ques_id'], user_ans=request.GET['u_ans'], right_ans=request.GET['r_ans'])
            obj.save()
            r = Reply(ques_id=request.GET['ques_id'])
            r.save()
        return JsonResponse({'data': 'done'})
