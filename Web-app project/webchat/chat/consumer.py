from channels.generic.websocket import  WebsocketConsumer, AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.utils import timezone

import json
import asyncio
from asgiref.sync import async_to_sync,sync_to_async

from .models import chatmsg
from .views import saving



   

class ChatConsumer(AsyncWebsocketConsumer):



    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )


        print("connect")
        await self.accept()
        
       
    async def disconnect(self, close_code):
        print("disconnect")
        await (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
            
        
        
     
        

    @database_sync_to_async
    def savin(self,text,nn,id1,id2):
        return chatmsg.saving(self,text=text,nn=nn,id1=id1,id2=id2)

        
  
        
        

        
    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name= text_data_json['name']
        id1= text_data_json['id1']
        id2= text_data_json['id2']
         
        rkr=await self.savin(message, name, id1, id2)
        te="saved"
        print(id1)
        await (self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message,
                'name' : name,
                'id1': id1,
                'id2': id2
            }
            
        )
   
    async def chat_message(self, event):
       
        nn=event.get('name' ,None)
        

        print("ctrceive", event)
        mss = event.get('message',None)
        id1= event.get('id1',None)
        id2= event.get('id2',None)
        
      
        
       
       
        await self.send(text_data=json.dumps({
            "type":"websocket.send",

            "message": mss,
            "id1": id1,
            "id2": id2



        })
        
        
        )
    


   
        


    
    


    
            

            


        
        


        
