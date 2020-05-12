from django.contrib import admin
from .models import Topic, Questions, Marksheet, Objection, Reply
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class ObjAdmin(ModelAdmin):
    list_display = [
        "user_id",
        "ques_id",
        "ques",
        "user_ans",
        "right_ans",
        "dateOfReport"
    ]

    def ques(self, obj):
        return Questions.objects.get(id=obj.ques_id).question


class ReplyAdmin(ModelAdmin):
    list_display = [
        "ques",
        "reply"
    ]

    def ques(self, obj):
        return Questions.objects.get(id=obj.ques_id).question


class QuestionAdmin(ModelAdmin):
    list_display = [
        "topic",
        "question",
        "answer"
    ]


class MarkAdmin(ModelAdmin):
    list_display = [
        "get_user",
        "topic_id",
        "mark",
        "right",
        "wrong",
        'passed',
    ]
    search_fields = ["user__username"]

    def get_user(self, obj):
        return obj.user.username

    get_user.admin_order_field = 'user__username'


class TopicAdmin(ModelAdmin):
    list_display = [
        "topic_name",
        "tpq",
        "published",
        "tTime"
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Marksheet, MarkAdmin)
admin.site.register(Objection, ObjAdmin)
admin.site.register(Reply, ReplyAdmin)
