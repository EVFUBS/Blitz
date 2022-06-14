from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=200)
    group_description = models.CharField(max_length=200, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)