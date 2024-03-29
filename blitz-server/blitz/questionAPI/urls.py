from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/answers/<int:pk>', views.QuestionsAnswers.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
    path('groups/', views.GroupList.as_view()),
    path('groups/user/', views.GroupUser.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('groups/submit/', views.SubmitGroup.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
