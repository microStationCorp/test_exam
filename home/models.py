from django.db import models
from django.utils import timezone

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=30)
    dateOfUpload = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic_name


class Questions(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.CharField(max_length=30)

    def __str__(self):
        return self.question


class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)