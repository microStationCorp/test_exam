from django.shortcuts import render, redirect
from home.models import Questions
from django.conf import settings

# Create your views here.


def qPaper(request, topic_id):
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
    else:
        que = Questions.objects.filter(topic__id=topic_id)
        return render(request, 'paper/paper.html', {'que': que, 'topic_id': topic_id})


def pSubmit(request, topic_id):
    if request.method == "POST":
        answer_sheet = []
        que = Questions.objects.filter(topic__id=topic_id)
        for i in range(len(que)):
            if request.POST.get(str(que[i].id)) == que[i].answer:
                res = True
            else:
                res = False
            answer_sheet.append({
                'ques': que[i].question,
                'ans': que[i].answer,
                'user': request.POST.get(str(que[i].id)),
                'rem': res,
            })
        return render(request, 'paper/markSheet.html', {'res': answer_sheet})
    else:
        return redirect("%s/timeline" % (settings.MAIN_URL))
