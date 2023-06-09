from django.shortcuts import render, redirect
from LoginApp.forms import UserForm, UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "LoginApp/index.html")

@login_required
def special(request):
    return HttpResponse('You are logged in now.')

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()


            registered = True

        else:
            print(user_form.errors, profile_form.errors,)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'LoginApp/registration.html', {'user_form':user_form,
                                                          'profile_form':profile_form,
                                                          'registered':registered,
                                                          })

def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect()
