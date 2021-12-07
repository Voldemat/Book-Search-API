from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import LoginForm, UserForm

# Create your views here.


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        # init form with post data
        form = LoginForm(request.POST)
        if form.is_valid():
            # init custom error
            form.user_error = ""
            
            # try to authentificate user with provided username and password
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse("books:search"))
                else:
                    form.user_error = "User is not active"
            else:
                form.user_error = 'User with given credentionals doesn`t exist.'
    return render(request, 'users/login.html', {'form': form})


def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("users:login"))
        else:
            print(form.errors)
    return render(request, 'users/signup.html', {'form': form})

def user_logout(request):
      logout(request)
      return redirect(reverse("users:login"))
