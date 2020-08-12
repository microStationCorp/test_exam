from django.contrib import admin
from .models import Topic, Questions, Marksheet, Objection, Reply, Subject
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import User

# Register your models here.


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(Objection)
class ObjAdmin(ModelAdmin):
    list_display = [
        "username",
        "ques",
        "user_ans",
        "right_ans",
        "dateOfReport"
    ]

    def ques(self, obj):
        return Questions.objects.get(id=obj.ques_id).question

    def username(self, obj):
        return User.objects.get(id=obj.user_id).username


@admin.register(Reply)
class ReplyAdmin(ModelAdmin):
    list_display = [
        "ques",
        "reply"
    ]

    def ques(self, obj):
        return Questions.objects.get(id=obj.ques_id).question


@admin.register(Questions)
class QuestionAdmin(ModelAdmin):
    list_display = [
        "topic",
        "question",
        "answer"
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs["queryset"] = Topic.objects.filter(published=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Marksheet)
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


@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    list_display = [
        "topic_name",
        "get_subject",
        "mark_sheets",
        "tpq",
        "published",
        "tTime"
    ]

    search_fields = ["subject__name"]

    def get_subject(self, obj):
        if obj.subject is None:
            return "no subject"
        else:
            return obj.subject.name

    def mark_sheets(self, obj):
        return Marksheet.objects.filter(topic_id=obj.id).count()
