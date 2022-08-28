from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('ragistration', views.ragistation, name='ragistation'),
    path('login' ,views.login , name='login'),
    path('action' ,views.action,name='action'),
    path('profile/<int:fid>',views.profile,name='profile'),
    path('profile/follow' ,views.follow,name='follow'),
    path('logout' ,views.logout,name='logout'),
    path('requestlist',views.requestl,name='requestl'),
    path('friendrequest',views.requestlist, name='requestlist'),
    path('friendrequest/accept/<int:fid>',views.friend,name='friend'),
    path('friendlist',views.friendship,name='friendship'),
    path('friendrequest/cancel/<int:fid>',views.cancel,name='cancel'),
    path('requestsent',views.sent,name='sent'),
    path('profile/chat/<str:room_name>',views.room,name="room"),
    path('chatlist', views.chatlist, name="chatlist"),
    path('index/posts', views.posts, name="posts"),
    path('index/likes/<int:pid>',views.likes,name="likes"),
    path('index/<int:fid>',views.index,name="index"),
    path('index/retweet/<int:pid>',views.retweet,name="retweet"),
    
    
    path('ap',views.rnam, name="rnam"),

  
    
    
]
