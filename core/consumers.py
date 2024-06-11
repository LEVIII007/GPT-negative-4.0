import json
import base64
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer
import core.INF.inference as inference


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


class captionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        pass

    # receive message from WebSocket
    async def receive(self, text_data):
        print("Received")
        text_data_json = json.loads(text_data)
        image_data = text_data_json['image']  # assuming the image data is base64 encoded

        # decode and process the image
        image_decoded = base64.b64decode(image_data)
        result = inference.process_image(image_decoded)  # process the image
        print(result)
        # send message to WebSocket
        await self.send(text_data=json.dumps({
            'result': result
        }))

