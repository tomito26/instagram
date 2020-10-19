from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name= models.CharField(max_length=60)
    caption = models.TextField()
    profile=models.ForeignKey('Profile',null=True,blank=True,on_delete=models.SET_NULL)
    likes = models.IntegerField(default=0,blank=True,null=True)
    comments = models.CharField(max_length=3000,blank=True,null=True)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
class Profile(models.Model):
    profile_photo =CloudinaryField('image')
    bio=models.TextField()
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    
    
