from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from account.forms import LoginForm, UserCreateForm


# Create your views here.
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect('Index')
        return render(request, 'form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('Index')


class CreateUserView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('Index')
        return render(request, 'form.html', {'form': form})
