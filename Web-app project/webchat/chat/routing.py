from django.urls import path, re_path
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumer import ChatConsumer
from channels.routing import route_pattern_match

websocket_urlpatterns = [
  url(r"^profile/chat/(?P<room_name>[\w.@+-]+)$", ChatConsumer.as_asgi()),

]
