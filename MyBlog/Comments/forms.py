from django import forms
from .models import Comment

class createCommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment    
        fields = ['content']