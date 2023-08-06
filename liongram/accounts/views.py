from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import UserCreateForm, SingUpForm
from users.models import User

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SingUpForm
        context = {'form': form }
        return render(request, 'accounts/signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SingUpForm(request.POST)

        if form.is_valid():
            # 회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            # 리다이렉트
            return redirect('accounts:signup')


# @login_required
# def login_view(request):
#     # GET, POST 분리
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid(): # 데이터 유효성 검사 (is_valid())
#             login(request, form.get_user()) # 비즈니스 로직 처리
#             return redirect('index')
#     else:
#         form = AuthenticationForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context) # 출력


def login_view(request):
    # GET, POST 분리
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        # 데이터 유효성 검사 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache) # 비즈니스 로직 처리
            # 응답
            return redirect('index')
        else:
            # 응답
            return render(request, 'accounts/login.html', {'form' : form}) # 출력   



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


