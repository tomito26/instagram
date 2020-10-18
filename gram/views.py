from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
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


def welcome(request):
    return render(request,'welcome.html')
