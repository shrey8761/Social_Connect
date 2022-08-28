"""
ASGI config for webchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

import chat.routing
from channels.auth import AuthMiddlewareStack

from channels.security.websocket import AllowedHostsOriginValidator


application = ProtocolTypeRouter({

    
    
    'websocket': AllowedHostsOriginValidator(

        AuthMiddlewareStack(
            URLRouter(
                
                    chat.routing.websocket_urlpatterns

                
            )
        )
    )
}
)


       

            
        
        
    


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings')


