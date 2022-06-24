from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    SignupForm,
    SigninForm
)
from django.contrib.auth import authenticate, login, logout
from .models import User


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            # 메시지 입력
            return redirect("index")
    else:
        form = SignupForm()
        
    context = {
        "form" : form
    }
    return render(request, "accounts/signup.html", context)

def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = get_object_or_404(User, email=email)
            if user is not None: # user가 있는지 체크
                if user.check_password(password): # password 검사
                    login(request, user)
                    return redirect("index")
    else:
        form = SigninForm(request.POST)
        
    context = {
        "form" : form
    }
    return render(request, "accounts/signin.html", context)

