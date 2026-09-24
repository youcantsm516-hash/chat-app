from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path('chat-list', views.chatlist, name='list'),
    path('chat/<uuid:uuid>', views.chat, name='chat'),
    path('new-chat', views.new_chat, name='new')
]