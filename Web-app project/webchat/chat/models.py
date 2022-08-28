from django.db import models
from django.utils import timezone

class Room(models.Model):
    name=models.TextField(null=False,unique=True)

class Message(models.Model):
    room=models.ForeignKey(Room,related_name='messages' , on_delete=models.CASCADE)
    msg=models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)



class chatmsg(models.Model):
    to_id=models.IntegerField(null=True,blank=True)
    fro_id=models.IntegerField(null=True,blank=True)
    msg=models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    roomname = models.TextField(blank=False,null=False)

    
    def saving(self,text,nn,id1,id2):
        krr=chatmsg.objects.create(roomname=nn,timestamp=timezone.now(),msg=text,fro_id=id1,to_id=id2)
        krr.save()
        return krr


# Create your models here.
