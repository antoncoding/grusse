# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth  # 別忘了import auth
#views.py
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .forms import CustomUserCreationForm, RegisterProfileForm, ProfileForm, CustomUserChangeForm

def login(request):
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/profile/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return render(request, 'registration/login.html') 

def index(request):
    # index login
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
    
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/profile/')
        else:
            return render(request, 'registration/login.html') 

    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        print('Get Post data')
        user_creation_form = CustomUserCreationForm(request.POST)   
        if user_creation_form.is_valid():
            user = user_creation_form.save()
            auth.login(request, user)
            user_form = CustomUserCreationForm(request.POST, instance=request.user)
            profile_form = RegisterProfileForm(request.POST or None, request.FILES or None, instance=request.user)
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/profile/')
        else:
            register_profile_form = RegisterProfileForm()    

    else:
        print('Render register')
        user_creation_form = CustomUserCreationForm()
        register_profile_form = RegisterProfileForm()
    return render(request, 'registration/register.html', locals())


def profile_page(request):
    return render(request, 'profile/profile.html', locals())


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponseRedirect('/secret/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'profile/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
