from django.contrib import admin
from .models import Topic, Questions, Options
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class QuestionAdmin(ModelAdmin):
    list_display = [
        "topic",
        "question",
        "answer"
    ]


admin.site.register(Topic)
admin.site.register(Questions,QuestionAdmin)
admin.site.register(Options)
