import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class GroupConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['group_code']   
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
         
    def receive(self, text_data):
        data_json = json.loads(text_data)
            
        if data_json['type'] == 'user_joined':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_joined',
                    'username': data_json['username'],
                    'points': data_json['points']
                }
            )
            
        elif data_json['type'] == 'start_quiz':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'start_quiz'
                }
            )
            
        elif data_json['type'] == 'start_question':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'start_question',
                    'answers': data_json['answers']
                }
            )
            
        elif data_json['type'] == 'end_question':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'end_question',
                    'answer': data_json['answer']
                }
            )
            
        elif data_json['type'] == 'end_quiz':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'end_quiz'
                }
            )
            
        elif data_json['type'] == 'score':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'score',
                    'username': data_json['username'],
                    'points': data_json['points']
                }
            )
        
    def user_joined(self, event):
        self.send(text_data=json.dumps({
            'type': 'user_joined',
            'username': event['username'],
            'points': event['points']
        }))
        
    def start_quiz(self, event):
        self.send(text_data=json.dumps({
            'type': 'start_quiz'
        }))
        
    def start_question(self, event):
        self.send(text_data=json.dumps({
            'type': 'start_question',
            'answers': event['answers']
        }))
        
    def end_question(self, event):
        self.send(text_data=json.dumps({
            'type': 'end_question',
            'answer': event['answer']
        }))
        
    def end_quiz(self, event):
        self.send(text_data=json.dumps({
            'type': 'end_quiz'
        }))
        
    def score(self, event):
        self.send(text_data=json.dumps({
            'type': 'user_score',
            'username': event['username'],
            'points': event['points']
        }))
            
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    