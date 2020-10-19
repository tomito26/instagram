from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name= models.CharField(max_length=60)
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    likes = models.IntegerField(default=0,blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey('Profile',on_delete=models.CASCADE,null=True,blank=True)
  
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
class Profile(models.Model):
    profile_photo =CloudinaryField('profile_photo')
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField()
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    
class Comments:
    comment=models.CharField(max_length=3000)
    image=models.ForeignKey('Image',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True,null=True,blank=True)
   
    def save_comment(self):
            self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments

    def __str__(self):
        return self.comment

