from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q, OuterRef, Subquery

# Create your views here.
@login_required(login_url="/users/login/")
def chat(request, uuid):
    currentChat = Chat.objects.get(id = uuid)
    messages = Message.objects.filter(chat = currentChat).order_by('-sentAt')
    if request.method == 'POST':
        form = forms.CreateMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = currentChat
            message.userFrom = request.user
            message.userTo = currentChat.userTo
            message.save()
            return redirect('chats:chat', uuid=currentChat.id)
    else:
        form = forms.CreateMessage()
    return render(request, 'chats/chat.html', { 'chat' : currentChat, 'messages' : messages, 'form' : form})

@login_required(login_url="/users/login/")
def chatlist(request):
    chats = Chat.objects.filter(Q(userFrom = request.user) | Q(userTo = request.user))
    latest_message = Message.objects.filter(
        chat=OuterRef('pk')
    ).order_by('-sentAt')

    chats = chats.annotate(
        latest_message_body=Subquery(
            latest_message.values('body')[:1]
        )
    )
    return render(request, 'chats/chats_list.html', {'chats': chats})

@login_required(login_url="/users/login/")
def new_chat(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = forms.StartChat(request.POST)
        if form.is_valid():
            selected_user = get_object_or_404(
                User,
                id=request.POST.get('user')
            )
            new_chat = Chat.objects.create(
                userFrom=request.user,
                userTo=selected_user
            )
            message = form.save(commit=False)
            message.chat = new_chat
            message.userFrom = request.user
            message.userTo = selected_user
            message.save()
            return redirect('chats:chat', uuid=new_chat.id)
    else:
        form = forms.StartChat()
    return render(request, 'chats/new_chat.html', {'users': users, 'form': form})