# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal

@purpose: handling all of the queueing processes for incoming events
"""

import queue
from event_handling.slack_event_processor import EventProcessor


class EventQueue():
    '''
    A weak Queue wrapper implementation to store event data in order to
    bypass the Slack API's multiple pings during long processing time.
    I don't want this here... but the Slack API offers no solution ;_;
    '''
    
    def __init__(self, client):
        self.event_queue = queue.Queue()
        self.client = client
        
    def start_processing(self):
        EventProcessor(self.event_queue, self.client).start()
        
    def put(self, event):
        if not self.event_queue.full():
            self.event_queue.put(event)
            return True
        return False
    
    def get(self):
        if not self.event_queue.empty():
            return self.event_queue.get()
        return None
    
    def task_done(self):
        if not self.event_queue.empty():
            self.event_queue.task_done()
            
    def join(self):
        self.event_queue.join()