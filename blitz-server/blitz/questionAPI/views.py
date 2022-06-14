from tokenize import group
from unicodedata import category
from django.shortcuts import render
from rest_framework import generics
from .models import Question, Answer, Group, Category
from .serializers import QuestionSerializer, AnswerSerializer, GroupSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GroupList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Group.objects.all()
        author = self.request.query_params.get('author', None)
        category = self.request.query_params.get('category', None)
        if author is not None:
            queryset = queryset.filter(author=author)
            return queryset
        if category is not None:
            queryset = queryset.filter(category_id=category)
        return queryset
    serializer_class = GroupSerializer
    
class SubmitGroup(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GroupSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GroupUser(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        queryset = Group.objects.filter(author=user)
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QuestionList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Question.objects.all()
        group = self.request.query_params.get('group')
        if group is not None:
            queryset = queryset.filter(group_id=group)
        return queryset
    serializer_class = QuestionSerializer
    
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class QuestionsAnswers(APIView):
    def get(self, request, pk):
        group = Group.objects.get(group_id=pk)
        questions = Question.objects.filter(group_id=group)
        questions_serializer = QuestionSerializer(questions, many=True)
        for question in questions_serializer.data:
            answers = Answer.objects.filter(question=question['question_id'])
            answers_serializer = AnswerSerializer(answers, many=True)
            question['answers'] = answers_serializer.data
        return Response(questions_serializer.data)
    
    def post(self, request, pk):
        questions = request.data
        group = Group.objects.get(group_id=pk)
        for question in questions:
            answers = question['answers']
            question.pop('answers')
            try:
                question_obj = Question.objects.get(question_id=question['question_id'])
                question_serializer = QuestionSerializer(question_obj, data=question)
                if question_serializer.is_valid():
                    q = question_serializer.save(group_id=group)
                    self.set_answers(answers, q)
            except Question.DoesNotExist:
                question_serializer = QuestionSerializer(data=question)
                if question_serializer.is_valid():
                    q = question_serializer.save(group_id=group)
                    self.set_answers(answers, q)
        return Response(status=201)
                    
    def set_answers(self, answers, question):
        for answer in answers:
            try:
                answer_obj = Answer.objects.get(answer_id=answer['answer_id'])
                #answer_obj.question = question.question_id
                answer_serializer = AnswerSerializer(answer_obj, data=answer)
                if answer_serializer.is_valid():
                    a = answer_serializer.save(question=question)
            except Answer.DoesNotExist:
                #answer['question'] = question.question_id
                answer_serializer = AnswerSerializer(data=answer)
                if answer_serializer.is_valid():
                    a = answer_serializer.save(question=question)
        
'''         questions = request.data
        for question in questions:
            answers = question['answers']
            question.pop('answers')
            if question['question_id'] is None:
                question_obj = Question.objects.get(question_id=question['question_id'])
                serializer = QuestionSerializer(question_obj, data=question)
                if serializer.is_valid():
                    serializer_obj = serializer.save()
                    self.setAnswers(answers, serializer_obj)
                    
            else:
                question['group_id'] = pk
                serializer = QuestionSerializer(data=question)
                if serializer.is_valid():
                    serializer_obj = serializer.save()
                    self.setAnswers(answers, serializer_obj)
                    
    def setAnswers(self, answers, serializer):
        for answer in answers:
            if answer['answer_id'] is None:
                answer_obj = Answer.objects.get(answer_id=answer['answer_id'])
                serializer = AnswerSerializer(data=answer)
                if serializer.is_valid():
                    serializer.save()
            else:
                answer['question'] = serializer.validated_data['question_id']
                serializer = AnswerSerializer(data=answer)
                if serializer.is_valid():
                    serializer.save() '''
                
            
        
'''     questions = request.data
        for question in questions:
            answers = question['answers']
            for answer in answers:
                print(answer)
                try:
                    if answer['answer_id'] is not None:
                        answer_object = Answer.objects.get(answer_id=answer['answer_id'])
                        answer_serializer = AnswerSerializer(answer_object, data=answer)
                        if answer_serializer.is_valid():
                            print(question['question_id'])
                            answer_serializer.save(question=question['question_id'])
                            print('Answer updated')
                        else:
                            print(answer_serializer.errors)
                            Response(answer_serializer.errors, status=400)
                    else:
                        answer_serializer = AnswerSerializer(data=answer)
                        if answer_serializer.is_valid():
                            answer_serializer.save(question=question['question_id'])
                            print('Answer created')
                except:
                    print('Error has occured')
            question.pop('answers')
            try:
                if question['question_id'] is not None:
                    question_object = Question.objects.get(question_id=question['question_id'])
                    question_serializer = QuestionSerializer(question_object, data=question)
                    if question_serializer.is_valid():
                        question_serializer.save(group_id=pk)
                        print('Question updated')
                    else:
                        Response(question_serializer.errors, status=400)
                else:
                    question_serializer = QuestionSerializer(data=question)
                    if question_serializer.is_valid():
                        question_serializer.save(group_id=pk)
                        print('Question created')
            except:
                print('Error has occured')
        return Response(status=201) '''
        
            
class AnswerList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Answer.objects.all()
        question = self.request.query_params.get('question')
        if question is not None:
            queryset = queryset.filter(question_id=question)
        return queryset
    serializer_class = AnswerSerializer
    
class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
