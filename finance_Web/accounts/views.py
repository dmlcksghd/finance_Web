from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth import views as auth_views
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():  # 폼이 유효한지 확인
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # 회원가입 후 대시보드로 리디렉션
        else:
            # 폼에 오류가 있을 경우, 에러와 함께 폼을 다시 보여줍니다.
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})