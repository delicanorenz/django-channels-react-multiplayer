# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Game

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'game_%s' % self.id
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def join(self):
        user = self.scope['user']
        game = Game.objects.get(id=self.id)
        game.users.add(user)
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'join',
                'user': user.username,
            }
        )
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    commands = {
        'join': join,
    }
