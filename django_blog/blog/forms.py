from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birthdate']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')

        #Ensure it includes validation rules as necessary.
        if not content or len(content.strip()) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        
        #validation: prevent overly long comments

        if len(content) > 500:
            raise forms.ValidationError("Comment cannot exceed 500 characters.")
        
        return content
        