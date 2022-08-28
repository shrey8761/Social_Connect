from django.shortcuts import render
from .models import update, userprofile, follow_model, friends, request_model, Room, Posts, lks, retw
from django.contrib.auth.models import auth
from django.contrib.auth.models import User


from django.utils import timezone
from django import template
from django.shortcuts import render,redirect
from chat.models import Room, Message,chatmsg
from django.utils import timezone
from .models import userprofile
from chat.models import chatmsg



reg=template.Library()




# Create your views here.
def home(request):
    upd = update.objects.last
    pst=Posts.objects.all()
   

    return render(request,'home.html',{'upd' : upd,'pst':pst})

def action(request):
    if request.method == 'POST' :
        nam=request.POST['seer']
        usr=userprofile.objects.filter(username__icontains=nam)
        po=request.POST['userna']
        pso=userprofile.objects.filter(username=po)
        pro=pso.first
        
        
        if usr is not None:
            return render(request,'index.html',{'ussr' : usr, 'user' : pro})
        else:
            return render(request , 'index.html',{'user' : pro})

    else:
        return render(request , 'index.html',{'user' : pro})


def login(request):
    bol = False
    upd =update.objects.first
    pst=Posts.objects.all()
    if request.method == 'POST':

        username=request.POST['name']
        password=request.POST['password']
        user = userprofile.objects.filter(username=username,password=password)
        
        
       

        
        if user is not None:
            
            use=user.first()
            idr = use.__getattribute__('id')
            lm=lks.objects.filter(Likes=idr)
            lkt=lm.values_list('plis_id',flat=True)
            

            
            
            
            
            print('loginShrey')

           

            
            
            return redirect('/index/{}'.format(idr))
            
        else :
            return render(request,'login.html',{'message' :'username does not exist'})
    else :
        return render(request ,'login.html')



        


   

    
def ragistation(request) :
    upd =update.objects.first

    if request.method == 'POST' :
    
       
        
           
        Username=request.POST['name']
        Firstname=request.POST['Firstname']
        Lastname=request.POST['Lastname']
         
        
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        country = request.POST['state']
        state = request.POST['city']
        image = request.FILES['image']
        resume = request.FILES['Resume']
        password= request.POST['password']
       
        dob =request.POST['birth_date']
        pincode =request.POST['pincode']
        if User.objects.filter(username=Username):
            return render(request,'ragistation.html',{'message' :'username already exists'})
        elif User.objects.filter(email=email) :
            return render(request,'ragistation.html',{'message' :'email already exists'})
        else:
            ussr=User.objects.create(username=Username,email=email,first_name=Firstname,last_name=Lastname,password=password)
            user = userprofile.objects.create(username=Username,firstname=Firstname,Lastname=Lastname,email=email,city=state,state=country,gender=gender,address=address,DOB=dob,image=image,resume=resume,pincode=pincode,password=password)
            ussr.save()
            user.save()


        
       
       
        return render(request,'home.html',{'upd' : upd})


    else:
        return render(request,'ragistation.html')

def profile(request,fid):
    
    ussr=userprofile.objects.filter(id=fid).first
   
    
    cuid=request.GET.get('id')
    user=userprofile.objects.filter(id=cuid)
    tys=follow_model.objects.filter(fro_id=fid,to_id=cuid).exists()
    fri=friends.objects.filter(to_id=fid,fro_id=cuid).exists()
    tr=False
    
    
    tg = False
    
    
    if tys :



        tg = True
        return render(request,'profile.html',{'user':user.first, 'ussr': ussr, 'tg':tg, 'tk':fri, 'tr':tr})
            
            
    else :
        tg = False
        return render(request,'profile.html',{'user':user.first, 'ussr': ussr, 'tg':tg, 'tk':fri, 'tr':tr})
    

def follow(request):

    cuid=request.POST['fro_usr'] 
    toid=request.POST['to_usr'] 
    btn=request.POST['cancel']
    

    user=userprofile.objects.filter(id=toid)
    ussr=userprofile.objects.filter(id=cuid).first
    res=request_model.objects.filter(to_id=toid,fro_id=cuid).exists()
    us=request_model.objects.filter(to_id=toid,fro_id=cuid)
    tys=follow_model.objects.filter(to_id=toid,fro_id=cuid).exists()
    tyu=follow_model.objects.filter(to_id=toid,fro_id=cuid)
    fri=friends.objects.filter(to_id=toid,fro_id=cuid).exists()
    fro=friends.objects.filter(to_id=toid,fro_id=cuid)
    sro=friends.objects.filter(fro_id=toid,to_id=cuid)
    
    tr=False
    if res:
        if btn == 'cancel':
            us.update(rejected=timezone.now())
        elif btn == 'follow':
            uset=request_model.objects.create(to_id=toid,fro_id=cuid)
            uset.save()
        elif btn == 'Follow':
            uset=request_model.objects.create(to_id=toid ,fro_id=cuid)
            uset.save()
            tr=True

    else :
        if btn == 'follow':
            uset=request_model.objects.create(to_id=toid,fro_id=cuid)
            uset.save()
        
            
        elif btn == 'Follow':
            
            uset=request_model.objects.create(to_id=toid ,fro_id=cuid)
            uset.save()
            tr=True

        



    
    
    if tys :
        tg = True
    else :
        tg = False
    
    if request.method == 'POST' :
        if btn == 'cancel':
            tyu.delete()
            
            tg= False
        elif btn == 'follow':

            
            tg=True

            if not tys:
                ty=follow_model.objects.create(to_id=toid ,fro_id=cuid)
                
                ty.save()
       
        elif btn == 'remove':
            fro.delete()
            sro.delete()
            
            fri=False
        
           

        return render(request,'profile.html',{'user':user.first, 'ussr': ussr, 'tg':tg, 'tk':fri, 'tr':tr})

    else :
        return render(request,'profile.html',{'user':user.first, 'ussr': ussr, 'tg':tg, 'tk':fri, 'tr':tr})

def logout(request):
    upd=update.objects.first
    return render(request,'home.html',{'upd' : upd})

user_model=userprofile()
def requestl(request):
    idt=request.GET.get('id')
    user=userprofile.objects.filter(id=idt).first
    
    friends=follow_model.objects.filter(fro_id=idt)
    users=[]
    for friend in friends:
        usr=userprofile.objects.filter(id=friend.to_id).first
        users.append(usr)
    return render(request,'friendlist.html',{'user':user, 'users':users})

def requestlist(request):
    idt=request.GET.get('id')
    user=userprofile.objects.filter(id=idt).first
    friends=follow_model.objects.filter(to_id=idt)
    us=request_model.objects.filter(to_id=idt)
    us.update(viewd=timezone.now())
    users=[]
    for friend in friends:
        usr=userprofile.objects.filter(id=friend.fro_id).first
        users.append(usr)
    return render(request,'requestrec.html',{'user':user, 'users':users})

def friend(request,fid):
    idt=request.GET.get('id')
    user=userprofile.objects.filter(id=fid).first
    frien=follow_model.objects.filter(to_id=fid)
   
    users=[]
    for friend in frien:
        usr=userprofile.objects.filter(id=friend.fro_id).first
        users.append(usr)
    tys=follow_model.objects.filter(to_id=fid,fro_id=idt)
    tys.delete()
    ty=friends.objects.filter(to_id=fid,fro_id=idt).exists()
    if not ty:
        


        fri=friends.objects.create(to_id=fid,fro_id=idt)
        frs=friends.objects.create(fro_id=fid,to_id=idt)
        fri.save()
        frs.save()
    return render(request,'requestrec.html',{'user':user, 'users':users})

def friendship(request):
    idt=request.GET.get('id')
    ty=friends.objects.filter(to_id=idt)
    user=userprofile.objects.filter(id=idt).first
    users=[]
    for friend in ty:
        usr=userprofile.objects.filter(id=friend.fro_id).first
        users.append(usr)
    return render(request,'friends.html',{'user':user, 'friends':users})

def cancel(request,fid):
    idt=request.GET.get('id')
    user=userprofile.objects.filter(id=fid).first
    frien=follow_model.objects.filter(to_id=fid)
    users=[]
    for friend in frien:
        usr=userprofile.objects.filter(id=friend.fro_id).first
        users.append(usr)
    tys=follow_model.objects.filter(to_id=fid,fro_id=idt)
    tys.delete()
    ty=friends.objects.filter(to_id=fid,fro_id=idt).exists()
    tyu=friends.objects.filter(to_id=fid,fro_id=idt)
    yt=friends.objects.filter(fro_id=fid,to_id=idt).exists()
    ytu=friends.objects.filter(fro_id=fid,to_id=idt)
    if ty:
        tyu.delete()
    if yt :
        ytu.delete()


       
    return render(request,'requestrec.html',{'user':user, 'users':users})
def sent(request):
    idt=request.GET.get('id')
    user=userprofile.objects.filter(id=idt).first
    friends=follow_model.objects.filter(fro_id=idt)
    users=[]
    for friend in friends:
        usr=userprofile.objects.filter(id=friend.to_id).first
        users.append(usr)
    return render(request,'friendlist.html',{'user':user, 'users':users})



def rnam(request):
    return render(request,'ap.html')

def room(request, room_name):
    idt=request.GET.get('fid')
    idr=request.GET.get('msger')
    msger=userprofile.objects.filter(id=idr).first()
    usr=userprofile.objects.filter(username=room_name).first()
    ussr=userprofile.objects.filter(id=idt).first()
    
    rk=chatmsg.objects.filter(roomname=room_name).exists()
    if not rk:
        kr=chatmsg.objects.create(roomname=room_name, fro_id=usr.id, to_id=idt)

    
    kr=chatmsg.objects.filter(roomname=room_name)
   
    meesages=reversed(kr.order_by('-timestamp'))
    print(room_name)
    
    
    return render(request, 'chat/room.html', {'room_name':room_name, 'mesg':meesages, 'usr':usr, 'ussr':ussr, 'msger':msger})

def chatlist(request):
    idt=request.GET.get('id')
    ty=friends.objects.filter(to_id=idt)
    user=userprofile.objects.filter(id=idt).first()
    
    users=[]
    for friend in ty:
        usr=userprofile.objects.filter(id=friend.fro_id).first()
       
        users.append(usr)

        
        
        
        
        
       
    
    return render(request,'chatlist.html',{'user':user, 'friends':users})

def posts(request):
    idt=request.GET.get('fid')
    upd = update.objects.last()
    user=userprofile.objects.filter(id=idt).first()
    pst=Posts.objects.all()
    
    
    
    if request.method == 'POST' :
        
        idr=request.POST['uid']
        usrt=userprofile.objects.filter(id=idr).first()
        msg=request.POST['post']
        usv=Posts.objects.create(posts=msg,use=idr,img=usrt.image, usname=usrt.username, Like=0, retweet=0)
        
        usv.save()
        
        lm=lks.objects.filter(Likes=idr)
        
        
        
        return redirect('/index/{}'.format(idr))

        
        
    else :
        return render(request, 'posts.html',{'user': user})

def likes(request,pid):
    idt=request.GET.get('fid')
    psts=Posts.objects.filter(id=pid).first()
    nm=psts.Like
    nt=int(nm)+1
    tn=int(nm)-1
    use=userprofile.objects.filter(id=idt).first()
    li=lks.objects.filter(Likes=idt,plis=psts).exists()
    lmd=lks.objects.filter(Likes=idt,plis=psts)
    
    if li :
        nt=Posts.objects.filter(id=pid).update(Like=tn)
        lj=lmd.delete()
    else :
        lik=lks.objects.create(Likes=idt,plis=psts)
        lnt=Posts.objects.filter(id=pid).update(Like=nt)
        lik.save()




    
    
    
    

    
    pst=Posts.objects.all()
    lm=lks.objects.filter(Likes=idt)
    lkt=lm.values_list('plis')
    rt=retw.objects.filter(retweet=idt)
    rtn=rt.values_list('plis_id',flat=True)
    
   
    
    return redirect('/index/{}'.format(idt))

def index(request,fid):
    use=userprofile.objects.filter(id=fid).first()
    lm=lks.objects.filter(Likes=fid)
    lkt=lm.values_list('plis_id',flat=True)
    rt=retw.objects.filter(retweet=fid)
    rtn=rt.values_list('plis_id',flat=True)
    pst=Posts.objects.all()
    rtw=retw.objects.all()
    km=rtw.values_list('plis_id',flat=True)
    psk=[]
    usv=[]
    ks=rtw.values_list('retweet',flat=True)
    for kq in ks:
        usv.append(userprofile.objects.filter(id=kq).first())
    usv.append(userprofile.objects.filter(id=22).first())
    for rw in km:
        psk.append(Posts.objects.filter(id=rw).first())
    psk.append(Posts.objects.filter(id=26).first())

    ps=zip(psk,usv)
     
        
    
    return render(request,'index.html',{'user' : use, 'pst':pst, 'lkt':lkt, 'rtn':rtn, 'psk':ps})

def retweet(request,pid):
    idt=request.GET.get('fid')
    psts=Posts.objects.filter(id=pid).first()
    nm=psts.retweet
    nt=int(nm)+1
    tn=int(nm)-1
    use=userprofile.objects.filter(id=idt).first()
    li=retw.objects.filter(retweet=idt,plis=psts).exists()
    lmd=retw.objects.filter(retweet=idt,plis=psts)
    
    if li :
        nt=Posts.objects.filter(id=pid).update(retweet=tn)
        lj=lmd.delete()
    else :
        lik=retw.objects.create(retweet=idt,plis=psts)
        lnt=Posts.objects.filter(id=pid).update(retweet=nt)
        lik.save()

    return redirect('/index/{}'.format(idt))




    
    
    
    

    
    pst=Posts.objects.all()
    lm=lks.objects.filter(retweet=idt)
    lkt=lm.values_list('plis')

@reg.filter
def pop_at(list, index):
    return list.pop(index)






    




    












 


    
    



    








 
  
  

            
        
    