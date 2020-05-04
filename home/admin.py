from django.contrib import admin
from .models import Topic, Questions, Marksheet
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class QuestionAdmin(ModelAdmin):
    list_display = [
        "topic",
        "question",
        "answer"
    ]


class MarkAdmin(ModelAdmin):
    list_display = [
        "user",
        "topic_id",
        "mark",
        "right",
        "wrong",
        'passed'
    ]


class TopicAdmin(ModelAdmin):
    list_display = [
        "topic_name",
        "tpq",
        "published",
    ]


admin.site.register(Topic,TopicAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Marksheet, MarkAdmin)
