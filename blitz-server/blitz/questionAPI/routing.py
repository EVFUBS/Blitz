from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/group/<str:group_code>/', consumers.GroupConsumer.as_asgi()),
]