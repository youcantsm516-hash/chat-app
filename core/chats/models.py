import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    userFrom = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chats_started',
        null = True,
        blank = True
    )
    userTo = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chats_received'
    )
    accepted = models.BooleanField(default=False)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    body = models.TextField()
    sentAt = models.DateTimeField(auto_now_add=True)
    userTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_received')
    userFrom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sent')