from django.urls import re_path 
# from ..gpt import consumers
from core import consumers


websocket_urlpatterns = [
    # re_path(r'ws/socket-server/', consumers.TranslationConsumer.as_asgi())
    re_path(r'ws/socket-server/', consumers.captionConsumer.as_asgi())
]