from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ImageForm,UserUpdateForm
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
    u_form = UserUpdateForm()
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST,instance=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and form.is_valid():
            u_form.save()
            form.save()
            messages.success(
                request,
                f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form =UserUpdateForm(request.POST,instance=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
    context = {
        'photos': photos,
        'profile_form':form,
        'u_form':u_form
    }
   
    return render(request,'registration/profile.html',context)

@login_required
def home(request):
    photos = Image.objects.all()
    profile = Profile.objects.all()
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'photos': photos,
        'form':form,
        'profile':profile
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
