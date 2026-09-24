from django import forms
from . import models

class CreateMessage(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['body']
        labels = {
            "body": "",
        }
        widgets = {
            "body": forms.Textarea(attrs={
                "class": "body-textarea",
                "rows": 3,
            }),
        }

class StartChat(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['body']
        labels = {
            "body": "",
        }
        widgets = {
            "body": forms.Textarea(attrs={
                "class": "newchat-textarea",
                "rows": 3,
            }),
        }