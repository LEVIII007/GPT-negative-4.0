"""
ASGI config for your_project_name project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import gpt.core.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gpt.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # your routing.py file path
            gpt.core.routing.websocket_urlpatterns
        )
    ),
})