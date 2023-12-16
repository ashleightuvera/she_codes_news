# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content',]
        widgets = {
            'pub_date': forms.DateInput(
            format= ['%d/%m/%Y %H:%M' ],
            attrs={
                'class':'form-control',
                'placeholder':'Select a date',
                'type':'datetime-local'
            }
        ),
    }