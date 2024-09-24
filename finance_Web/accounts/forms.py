# 사용자 등록

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, requred=True, help_text='유효한 이메일 주소를 입력하세요.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')