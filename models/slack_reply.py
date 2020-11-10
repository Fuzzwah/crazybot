# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
"""


class Reply():
    '''
    A wrapper object for a Slack reply, allows for
    custom functions and bodies based off of the user being
    replied to
    '''
    def __init__(self, event, function=None, args=None, body=None):
        self.client = event.client
        self.channel = event.channel
        self.thread_ts = event.timestamp
        self.reply_user = event.username
        self.function = function
        self.args = args
        #self.d_function = d_function
        self.body = body
    
    def apply_function(self):
        return self.function(self.args)
    
    def direct_function(self):
        return self.d_function()
    
        
    def send(self):
        if self.body is not None and self.function is not None:
            body = self.apply_function()+self.body
        elif self.body is not None:
            body = self.body
        elif self.function is not None:
            body = self.apply_function()
        else:
            #raise invalid input error
            return
        
        return self.client.chat_postMessage(
                                channel=self.channel,
                                thread_ts=self.thread_ts,
                                text=body)
        
        
        
