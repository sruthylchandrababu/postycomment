from .models import Post
from django import forms
class ModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post_name','post','date']