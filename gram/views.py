from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ImageForm
from .models import Image,Profile
# from .email import send_welcome_email
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data['email']
            # send_welcome_email(username,email)
            messages.success(
                request,
                f'Your account has been created!You are now able to login')
            return redirect('home')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/registration.html', context)

@login_required
def profile(request):
    photos = Image.objects.all()
    profile_info = Profile.objects.all()
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')


    context = {
        'photos': photos,
        'profile_form':form
    }
   
    return render(request,'registration/profile.html',context)

@login_required
def home(request):
    photos = Image.objects.all()
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'photos': photos,
        'form':form
    }
    return render(request, 'insta/home.html', context)


def load(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'insta/load.html', context)
