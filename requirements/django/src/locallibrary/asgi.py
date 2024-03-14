"""
ASGI config for locallibrary project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
import web_sockets.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
os.environ.setdefault('SERVER_GATEWAY_INTERFACE', 'Asynchronous')

#application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'https': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
                web_sockets.routing.urlpatterns
            ])
        )
})
