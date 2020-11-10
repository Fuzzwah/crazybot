# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
"""

from event_handling.slack_event_queue import EventQueue
from event_handling.slack_event import Event

class EventHandler():
    '''
    Wraps events and adds them to EventQueue
    '''
    def __init__(self, client):
        self.client = client
        self.queue = EventQueue(self.client)
        
    def handle(self, payload):
        event = self.wrap_event(payload)
        self.queue.put(event)
        self.queue.start_processing()
        
    def wrap_event(self, payload):
        event = Event(self.client, payload)
        return event
        

        


