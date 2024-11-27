from django.shortcuts import render, redirect
from .forms import registrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage

# Create your views here.
def registration_view(request):
    form = registrationForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] != data['again_password']: #validating the password matching
            form = registrationForm()
            return render(request, "login/register.html", context={
                    "form": form,
                    "warning": "Passwords do not match. Please try again."
                })
        else:
            try: #trying to save the user, if same username already taken then load blank form
                new_user = User.objects.create_user(
                    username = data['username'],
                    email = data['email'],
                )
                new_user.set_password(data['password'])
                new_user.save()
            except:
                form = registrationForm()
                return render(request, "login/register.html", context={
                        "form": form,
                        "warning": "User with same username already exists"
                    })
            return redirect('create_profile')
    return render(request, 'login/register.html', context={"form": form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        if not User.objects.filter(username = username).exists():
            return render(request, "login/login.html", context={
                    "form": form,
                    "warning": "User does not exist"
                })
        user = authenticate(username = username, password = password)
        if user == None:
            return render(request, "login/login.html", context={
                    "form": form,
                    "warning": "Passwords do not match. Please try again."
                })
        else:
            login(request, user)
            return redirect('landing:index')
    return render(request, 'login/login.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing:index')

def profile_creation(request):  
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            image = request.FILES.get('image')
            user = User.objects.filter(username = data['username']).first()
            if image :
                new_profile = Profile.objects.create(
                    user = user,
                    image = image,
                    location = data['loc']
                )
            else:
                new_profile = Profile.objects.create(
                    user = user,
                    location = data['loc']
                )
            new_profile.save()
            return redirect('login')
    else:
        form = ProfileForm()
    return render(request, 'login/register.html', context={'form':form})

def profile_view(request):
    return render(request, 'login/profile.html', context={})