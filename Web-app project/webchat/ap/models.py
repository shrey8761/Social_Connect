from django.db import models
from django.utils import timezone
from django import template

register = template.Library()

# Create your models here
class update (models.Model):
    happyc = models.IntegerField()
    Solutions = models.IntegerField()
    hos = models.IntegerField()
    team = models.IntegerField()

class userprofile (models.Model):
    username = models.CharField(max_length=100,null=False)
    firstname=  models.CharField(max_length=100,null=False)
    Lastname=  models.CharField(max_length=100,null=False)
    email = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    address = models.TextField(max_length=200)
    DOB = models.DateField()
    image = models.FileField(upload_to='pics',null = True ,blank = True)
    resume = models.FileField(upload_to='resume' ,null=True,blank=True)
    pincode = models.CharField(max_length=10)
    password= models.TextField(max_length=100)

    @register.tag(name="filter_uk")
    def filter_uk(uid):
        resu=userprofile.objects.filter(id=uid).first()
        return resu

class follow_model(models.Model):
    created=models.DateTimeField(default=timezone.now)
    to_id=models.IntegerField(null=False)
    fro_id=models.IntegerField(null=False)

class friends(models.Model):
    created=models.DateTimeField(default=timezone.now)
    to_id=models.IntegerField(null=False)
    fro_id=models.IntegerField(null=False)

class request_model(models.Model):
    created=models.DateTimeField(default=timezone.now)
    rejected=models.DateTimeField(blank=True,default=timezone.now)
    viewd=models.DateTimeField(blank=True,default=timezone.now)
    to_id=models.IntegerField(null=False)
    fro_id=models.IntegerField(null=False)
class following_model(models.Model):
    created=models.DateTimeField(default=timezone.now)
    to_id=models.IntegerField(null=False)
    fro_id=models.IntegerField(null=False)
class Room(models.Model):
    name=models.TextField()
class Message(models.Model):
    room=models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    message=models.TextField()
    Timestamp=models.DateTimeField(auto_now_add=True)

class Posts(models.Model):
    posts = models.TextField(null=True)
    use = models.IntegerField()
    Like = models.IntegerField(null=True)
    retweet= models.IntegerField(null=True)
    
   
    rep = models.TextField(null=True)
    img= models.FileField(null=True)
    usname=models.TextField(null=True)
    comm = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class lks(models.Model):
    
    
    Likes = models.IntegerField(null=True)  
    plis=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True) 
class reps(models.Model):
    Replies = models.IntegerField(null=True)
    plis=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True)

class retw(models.Model):
    retweet = models.IntegerField(null=True)
    plis=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True)












    


    
    

    
    


    
