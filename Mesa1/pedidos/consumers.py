# pedidos/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Pedido

class PedidoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("pedidos", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("pedidos", self.channel_name)

    def receive(self, text_data):
        pedido_data = json.loads(text_data)
        Pedido.objects.create(**pedido_data)
        async_to_sync(self.channel_layer.group_send)(
            "pedidos",
            {
                "type": "pedido_message",
                "pedido": pedido_data,
            },
        )

    def pedido_message(self, event):
        pedido_data = event["pedido"]
        self.send(text_data=json.dumps(pedido_data))
