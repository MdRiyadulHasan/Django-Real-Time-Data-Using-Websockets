from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'test-consumer'
        self.room_group_name = "test-consumer-group"

        async_to_sync(self.channel_layer.group_add)(
             self.room_group_name, self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({"status":"connectecd from django channels"}))
    def receive(self, text_data=None, bytes_data=None):
       print(text_data)
       self.send(text_data=json.dumps({"msg":"we got you"}))
    def disconnect(self, *args, **kwargs):
        print("Channel Layer ..", self.channel_layer)

        print("Channel Name ..", self.channel_name)

        async_to_sync (self.channel_layer.group_discard)(
            "programmers", self.channel_name
        )

        print("disconnected .....")
        # raise StopConsumer()

    def send_notification(self,event):
        print(event)
        print(event.get('value'))
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({"payload":data}))
        print("send notification")


class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'test-consumer'
        self.room_group_name = "test-consumer-group"

        await (self.channel_layer.group_add)(
             self.room_group_name, self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({"status":"connectecd from django channels async "}))

    async def receive(self, text_data=None, bytes_data=None):
    #    print(text_data)
       await self.send(text_data=json.dumps({"msg":"we got you"}))
    async def disconnect(self, *args, **kwargs):

        print("disconnected .....")
        raise StopConsumer()

    async def send_notification1(self,event):
        # print(event)
        print(event.get('value'))
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({"payload":data}))
        # print("send notification")