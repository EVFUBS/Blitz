from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<str:username>/', views.UserByName.as_view()),
    path('currentUser/', views.getUserInfo),
    path('token/', obtain_auth_token),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('csrf/', views.csrf_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
