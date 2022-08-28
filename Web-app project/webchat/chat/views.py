from django.shortcuts import render
from .models import Room, Message,chatmsg
from django.utils import timezone
from ap.models import userprofile

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    idt=request.GET.get('fid')
    msger=userprofile.objects.filter(id=idr).first()
    
    usr=userprofile.objects.filter(username=room_name).first()
    ussr=userprofile.objects.filter(id=idt).first()
    rk=chatmsg.objects.filter(roomname=room_name).exists()
    if not rk:
        kr=chatmsg.objects.create(roomname=room_name,to_id=idt)
    
    krs=chatmsg.objects.filter(roomname=room_name)
    
    meesages=reversed(krs.order_by('-timestamp'))
    print(room_name)
    
    
    
    return render(request, 'chat/room.html', {'room_name':room_name, 'mesg':meesages, 'usr':usr, 'ussr':ussr, 'msger':msger})

def saving(text,rname):
    krr=chatmsg.objects.create(roomname=rname,timestamp=timezone.now(),msg=text)
    krr.save()




