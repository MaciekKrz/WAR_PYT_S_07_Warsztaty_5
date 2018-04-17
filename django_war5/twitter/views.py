from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.list import ListView
from .forms import TweetModelForms, LoginForm, AddUserForm
from .models import Tweet



class BaseView(View):
    def get(self, request):
        return render(
            request,
            template_name="base_page.html",
            )



class MainPageView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        if request.user.is_authenticated:
            user_id = request.user.id
        ctx = {"tweets": tweets,
               "user_id": user_id}
        return render(request,
                      template_name="main_page.html",
                      context=ctx)


class AddTwitterView(View):
    def get(self, request):
        form = TweetModelForms()
        ctx = {"form": form}
        return render(request,
                      template_name="add_tweet.html",
                      context=ctx)

    def post(self, request):
        form = TweetModelForms(request.POST)
        if form.is_valid():
            form.save()
            # last_name = form.cleaned_data['last_name']
            # found_studends = Student.objects.filter(last_name__icontains=last_name)
            return redirect(reverse("main"))


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        ctx = {
            'form': form
        }
        return render(
            request,
            "add_user.html",
            ctx
        )
    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if User.objects.filter(username=login).exists():
                form.add_error('login', "Taki login jest już zajęty")
            if password != password2:
                form.add_error('password', "Hasło musi być identyczne")
            if not form.errors:
                User.objects.create_user(login,
                                         email,
                                         password,
                                         first_name=first_name,
                                         last_name=last_name)
                return HttpResponse("Udało utworzyć się nowego użytkownika")
        ctx = {
            'form': form
        }
        return render(
            request,
            "add_user.html",
            ctx
        )


class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            "form": form
        }
        return render(
            request,
            "login.html",
            ctx
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("main"))
            else:
                return HttpResponse("HUJOWOW")


class LogoutUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse("main"))


class UserView(View):
    def get(self, request, user_id):
        user = User.objects.filter(id=user_id)
        return render(request, "user.html", {"user": user})
