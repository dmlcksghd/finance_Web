from django.shortcuts import render
from django.contrib.auth import login
from .forms import SighupForm
from django.contrib.auth import views as auth_views
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)    # 회원가입 후 자동 로그인
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('dashboard')    # 로그인 후 이동할 페이지
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

