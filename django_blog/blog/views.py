from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import Post
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #save new user
            login(request, user) #then log the user in after registration
            return redirect('/') #redirect to home or success page
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
            return redirect('home')
            
    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect back to profile after saving

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'blog/profile.html', context)