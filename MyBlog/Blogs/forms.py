from django import forms
from .models import Blog

class createBlogForm(forms.ModelForm):
    
    class Meta():
        model = Blog    
        fields = ['title','content','thumbNail']