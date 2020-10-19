from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image,Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','caption','likes','comments']
        
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'