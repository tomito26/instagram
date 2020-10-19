from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ImageForm
from .models import Image,Profile
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Your account has been created!You are now able to login')
            return redirect('welcome')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/registration.html', context)

def profile(request):
    return render(request,'registration/profile')

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
