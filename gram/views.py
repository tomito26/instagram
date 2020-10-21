import pdb
from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CommentsForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,ImageForm,UserUpdateForm
from .models import Image,Profile,Comments
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
  
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request,
                f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
     
    context = {
        'photos': photos,
        'p_form':p_form,
        'u_form':u_form
    }
   
    return render(request,'registration/profile.html',context)

@login_required
def home(request):
    photos = Image.objects.all()
    profile = Profile.objects.all()
    form = ImageForm()
    users = User.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'photos': photos,
        'form':form,
        'profile':profile,
        'users':users
    }
    return render(request, 'home.html', context)



def post(request,image_id):
    image = Image.objects.get(id=image_id)
    comments = Comments.objects.all()
    commentform = CommentsForm()
    if request.method == 'POST':
        commentform=CommentsForm(request.POST)
        if commentform.is_valid():
            content = commentform.fields['comment']
            new_comment=Comments(comment=content,image=image,user=request.user)
            new_comment.save()
            
            context={
                'new_comment':new_comment
            }
            return redirect('home',context)
    
    context = {
        
        'commentform':commentform,
        'image':image,
        'comments':comments
    }
    
    return render(request,'comment.html',context)


def search_results(request):
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get("pic")
        searched_images=Image.search_by_name(search_term)
        message = f"{search_term}"
        
        context= {
            'message':message,
            'image':searched_images
        }
        return render(request,'search.html',context)
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{'message':message})