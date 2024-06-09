import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer
import gpt.core.INF.inference as inference

class TranslationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sentence = text_data_json['sentence']

        # Use your inference module to process the sentence
        translation = inference.translate(inference.model, sentence)

        # Send the translation back to the WebSocket
        await self.send(text_data=json.dumps({
            'translation': translation
        }))
