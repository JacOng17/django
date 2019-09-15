from django import forms

from .models import Post

# PostForm is the name of our form & is a ModelForm
class PostForm(forms.ModelForm):

  class Meta:
      # Telling Django which model to use to create this form
      model = Post
      
      # We want only these fields to end up on our form
      fields = ('title', 'text',)