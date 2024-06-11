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


import base64
from PIL import Image
import io

class captionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        pass

    # receive message from WebSocket
    async def receive(self, text_data = None, bytes_data= None):
        print("Received :", bytes_data)
        if bytes_data is not None:
            image = Image.open(io.BytesIO(bytes_data))
            print(image)
            result = inference.process_image(image)  # process the image
            print(result)
            # send message to WebSocket
            await self.send(text_data=json.dumps({
                'result': result
            }))
        else:
            print("No data received")
            await self.send(text_data=json.dumps({
                'result': "No data received"
            }))