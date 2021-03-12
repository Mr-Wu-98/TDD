from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    # 外键约束？就是说，定义了一个关系。每个Choice对象都要关联到一个Question对象
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
