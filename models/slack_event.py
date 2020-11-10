# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
"""
from internal_utils import user_utils

class Event():
    '''
    A wrapper object for slack event data
    '''
    def __init__(self, client, payload):
        self.client = client
        self.event = payload.get('event',{})
        self.bot_id = self.event.get('bot_id')
        self.user_id = self.event.get('user')
        self.username = user_utils.get_username(self.client, self.user_id)
        self.event_type = self.event.get('type')
        
        self.set_fields_by_type()
            
    def set_fields_by_type(self):
        if self.event_type == 'message':
            self.channel = self.event.get('channel')
            self.content = self.event.get('text')
            self.timestamp = self.event.get('ts')
        elif self.event_type == 'reaction_added':
            self.channel = self.event.get('item',{}).get('channel')
            self.content = self.event.get('reaction')
            self.timestamp = self.event.get('item',{}).get('ts')
    