import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import mainApp.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websockets.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':URLRouter(
        mainApp.routing.websocket_urlpatterns
        # chat.routing.websocket_urlpatterns +
        # Practice.routing.websocket_urlpatterns
    )
    
})