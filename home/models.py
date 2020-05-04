from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=30)
    dateOfUpload = models.DateTimeField(default=timezone.now)
    tTime = models.IntegerField(default=0)
    tpq=models.IntegerField(default=15)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.topic_name


class Questions(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    answer = models.CharField(max_length=30)

    def __str__(self):
        return self.question


class Marksheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.IntegerField(default=0)
    mark = models.IntegerField(default=0)
    total_q = models.IntegerField(default=0)
    right = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    notA = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    passed = models.BooleanField(default=False)
