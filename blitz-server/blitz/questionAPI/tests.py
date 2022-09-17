import json
from unicodedata import category

from authAPI.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.test import APITestCase

from .models import Answer, Category, Group, Question
from .serializers import (AnswerSerializer, CategorySerializer,
                          GroupSerializer, QuestionSerializer)


# Create your tests here.
class TestQuestionAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="test", password="test", email="")
        self.client.login(username="test", password="test")
        
        self.category = {
            'catergory_name': 'Test Category',
        }
        self.category_serializer = CategorySerializer(data=self.category)
        if self.category_serializer.is_valid():
            self.category_serializer.save()
        
        self.group = {
            'group_name': 'Test Group',
            'group_description': 'Test Group Description',
            'category_id': self.category_serializer.data['category_id'],
            'author': User.objects.get(username="test"),
        }
        self.group_serializer = GroupSerializer(data=self.group)
        if self.group_serializer.is_valid():
            self.group_serializer.save()
            
        self.group2 = {
            'group_name': 'Test Group 2',
            'group_description': 'Test Group Description 2',
            'category_id': self.category_serializer.data['category_id'],
            'author': User.objects.get(username="test"),
        }
        self.group2_serializer = GroupSerializer(data=self.group2)
        if self.group2_serializer.is_valid():
            self.group2_serializer.save()
            
        self.question = {
            'question_text': 'Test Question',
            'group_id': self.group_serializer.data['group_id'],
        }
        self.question_serializer = QuestionSerializer(data=self.question)
        if self.question_serializer.is_valid():
            self.question_serializer.save()
            
        self.answer1 = {
            'question': self.question_serializer.data,
            'answer_text': 'Test Answer 1',
            'correct': True,
        }
        self.answer2 = {
            'question': self.question_serializer.data,
            'answer_text': 'Test Answer 2',
            'correct': False,
        }
        self.answer1_serializer = AnswerSerializer(data=self.answer1)
        self.answer2_serializer = AnswerSerializer(data=self.answer2)
        if self.answer1_serializer.is_valid() and self.answer2_serializer.is_valid():
            self.answer1_serializer.save()
            self.answer2_serializer.save()
    
    def question_list(self):
        response = self.client.get('/api/quiz/question/')
        self.assertEqual(response.status_code, 200)
    
    def question_detail(self):
        response = self.client.get('/api/quiz/question/1/')
        self.assertEqual(response.status_code, 200)
        
    def question_answers(self):
        response = self.client.get('/api/quiz/question/answers/1/')
        self.assertEqual(response.status_code, 200)
        
        data = [
            {
                'question_text': 'Test Question',
                'group_id': 2,
                'answers': [
                    {
                        'answer_text': 'Test Answer 1',
                        'correct': True,
                        'question': None,
                    },
                    {
                        'answer_text': 'Test Answer 2',
                        'correct': False,
                        'question': None,
                    }
                ]
            },
            {
                'question_text': 'Test Question',
                'group_id': 2,
                'answers': [
                    {
                        'answer_text': 'Test Answer 1',
                        'correct': True,
                        'question': None,
                    },
                    {
                        'answer_text': 'Test Answer 2',
                        'correct': False,
                        'question': None,
                    },
                    {
                        'answer_text': 'Test Answer 3',
                        'correct': False,
                        'question': None,
                    }
                ]
            }
        ]
        self.client.post('/api/quiz/question/answer/2/', data)
        
        
    