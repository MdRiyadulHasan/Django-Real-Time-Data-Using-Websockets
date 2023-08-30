from django.urls import path
from . import consumers

websocket_urlpatterns  =[
    path ('ws/sc/', consumers.TestConsumer.as_asgi()),
    path ('ws/ac/', consumers.NewConsumer.as_asgi()),
    # path('ws/ac/', consumers.myASyncConsumer.as_asgi()),
]