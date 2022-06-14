from rest_framework import serializers
from .models import Question, Answer, Group, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_id', 'group_name', 'group_description', 'category_id', 'author')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
