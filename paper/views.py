from django.shortcuts import render, redirect
from home.models import Questions, Marksheet, Topic
from django.conf import settings

# Create your views here.


def qPaper(request, topic_id):
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
    elif len(Marksheet.objects.filter(user=request.user, topic_id=topic_id)) != 0:
        return redirect("%s/timeline" % (settings.MAIN_URL))
    else:
        t = Topic.objects.get(id=topic_id)
        que = Questions.objects.filter(topic__id=topic_id)
        if t.tTime == 0:
            t.tTime = len(que)*15
            t.save()
        return render(request, 'paper/paper.html', {'que': que, 'topic_id': topic_id, 't': t})


def pSubmit(request, topic_id):
    if request.method == "POST" and len(Marksheet.objects.filter(user=request.user, topic_id=topic_id)) == 0:
        answer_sheet = []
        right = 0
        notA = 0
        wrong = 0
        que = Questions.objects.filter(topic__id=topic_id)
        for i in range(len(que)):
            if request.POST.get(str(que[i].id)) == que[i].answer:
                res = True
                right += 1
            elif request.POST.get(str(que[i].id)) == None:
                notA += 1
                res = None
            else:
                wrong += 1
                res = False
            answer_sheet.append({
                'ques': que[i].question,
                'ans': que[i].answer,
                'user': request.POST.get(str(que[i].id)),
                'rem': res,
            })

        result = {
            'right': right,
            'wrong': wrong,
            'notA': notA,
            'total': len(que),
            'mark': (right-wrong*0.25),
            'perc': ((right-wrong*0.25)/len(que))*100,
        }

        if result['perc'] >= 40:
            result['rem'] = True
        else:
            result['rem'] = False

        # m = Marksheet(user=request.user, topic_id=topic_id, mark=result['mark'], total_q=result['total'],
        #               right=result['right'], wrong=result['wrong'], notA=result['notA'], percentage=result['perc'], passed=result['rem'])
        # m.save()

        return render(request, 'paper/markSheet.html', {'ans': answer_sheet, 'res': result})
    else:
        return redirect("%s/timeline" % (settings.MAIN_URL))


def pResult(request, topic_id):
    ms = Marksheet.objects.get(user=request.user, topic_id=topic_id)
    t = Topic.objects.get(id=topic_id)
    return render(request, 'paper/result.html', {'res': ms, 'topic': t})
