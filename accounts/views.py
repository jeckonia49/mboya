from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from django.http import HttpResponseRedirect
from accounts.auth.forms import (
    LoginForm,
)
from .models import AccountUser
from django.contrib.auth import authenticate, login, logout




class LoginView(View):
    login_form = LoginForm
    def post(self, request, *args, **kwargs):
        form = self.login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = authenticate(request, username=email,
                                 password=form.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
