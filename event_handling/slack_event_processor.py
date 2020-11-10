# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal

@purpose: run a processing thread for the event queue
"""

import threading
from models import slack_reply
from internal_utils import custom_reply

class EventProcessor(threading.Thread):
    '''
    Event processing thread, runs throught the event queue and
    processes every event in a separate thread so that the event_listener
    can return OK on time. Thanks again Slack API :)
    '''
    def __init__(self, event_queue, client, *args, **kwargs):
        self.event_queue = event_queue
        self.client = client
        super().__init__(*args, **kwargs)
    
    def run(self):
        while True:
            while not self.event_queue.empty():
                self.assign_event_process(self.event_queue.get())
        self.event_queue.join()
        
    def assign_event_process(self, event):
        if event.event_type == 'reaction_added':
            self.process_reaction(event)
        elif event.event_type == 'message':
            self.process_message(event)
            
    def process_reaction(self, event):
        if event.bot_id == None:
            if event.content == 'robot_face':
                slack_reply.Reply(event, custom_reply.get_personal_reaction_reply).send()
                self.event_queue.task_done()
        
    def process_message(self, event):
        if event.event.get('thread_ts') is None and event.bot_id is None: 
            slack_reply.Reply(event, custom_reply.get_personal_message_reply, event.username).send()
            self.event_queue.task_done()

