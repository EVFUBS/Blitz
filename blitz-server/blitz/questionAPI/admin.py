from django.contrib import admin
from .models import Question, Answer, Group, Category

# Register your models here.
admin.register(Question)
admin.register(Answer)
admin.register(Group)
admin.register(Category)