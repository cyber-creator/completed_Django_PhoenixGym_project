from django import forms
from django.contrib.auth.models import User

from gym.models import Blog
from .models import ProfileCoach


class FormRegister(forms.ModelForm):
    password_confirm = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')


# class FormLogin(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField()


class FormProfile(forms.ModelForm):

    class Meta:
        model = ProfileCoach
        fields = ('first_name', 'biography', 'avatar', 'instagram', 'facebook', 'youtube')


class FormUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name',)


class BlogEditForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'blog_text', 'special_text', 'blog_text_next', 'youtube_link')
