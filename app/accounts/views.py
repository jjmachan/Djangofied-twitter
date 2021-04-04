from django.shortcuts import render, redirect
from .forms import NewUserForm, NewTweetForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.utils import timezone
from .models import Tweet

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            txt = form.cleaned_data.get('tweet_text')
            user = request.user
            user.tweet_set.create(tweet_text=txt)
            redirect('home')
            print('tweeted!')
    form = NewTweetForm
    tweets = Tweet.objects.order_by('-tweet_date')
    return render(request, 'accounts/home.html',
                  {'post_tweet': form,
                   'tweets': tweets})

def sign_up(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registeration successful.")
            print('success')
            return redirect("home")
        messages.error(request, "Unsuccessful registeration. Invalid fields")
    form = NewUserForm
    return render(request, 'registration/sign_up.html',
            {"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "invalid username or password")

    form = AuthenticationForm()
    return render(request=request,
                  template_name='registration/login.html',
                  context={'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('home')
