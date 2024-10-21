from django import forms
from .models import Tweet

class TweetForm (forms.modelForm):
    class Meta : 
        model = Tweet
        fields = ['text','photo']