# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 01:26:23 2020

@author: Matt
"""
import time
import os
from models import slack_reply as sr
from internal_utils import date_util

class BinaryVote():
    '''
    Poll w only 2 choices
    '''
    def __init__(self, event, theme, voting_time, y_emoji=None, n_emoji=None):
        self.event = event
        self.theme = theme
        self.vt = voting_time
        self.set_emojis(y_emoji, n_emoji)
    
    def set_emojis(self, y_emoji, n_emoji):
        if y_emoji is None and n_emoji is None:
            self.yes = '+1'
            self.no = '-1'
        elif y_emoji is None:
            self.yes = '+1'
            self.no = n_emoji
        elif n_emoji is None:
            self.yes = y_emoji
            self.no = '-1'
        else:
            self.yes = y_emoji
            self.no = n_emoji
            
    def run(self):
        poll = sr.Reply(self.event, function=self.create_poll_message).send()
        yes, no = self.count_votes(poll.get('ts'))
        results = self.create_results_message(yes, no)
        results = sr.Reply(self.event, body=results).send()
        
            
    def create_poll_message(self, username):
        reply = 'You have initiated a '+self.theme+' poll. Please react to this message with :'+self.yes+': to vote '+username.capitalize()+'\'s statement a '+self.theme+' or with :'+self.no+': to vote the statement not a '+self.theme+'.'
        return reply
        
        
    def count_votes(self, timestamp):
        time.sleep(self.vt)
        return self.binary_vote_counter(timestamp)
        
    def binary_vote_counter(self, poll_timestamp):
        reactions = self.event.client.reactions_get(channel=self.event.channel, timestamp=poll_timestamp)
        yes_count = 0
        no_count = 0
        if reactions.get('message',{}).get('reactions') != None:
            for reaction in reactions.get('message',{}).get('reactions'):
                vote = reaction['name']
                if vote == self.yes:
                    yes_count += reaction.get('count')
                elif vote == self.no:
                    no_count += reaction.get('count')
        return yes_count, no_count
        
    def create_results_message(self, yes_count, no_count):
        y_maj = 'This statement has been ruled a '+self.theme+', '+str(yes_count)+' to '+str(no_count)+'.'
        n_maj = 'This statement has been ruled not a '+self.theme+', '+str(no_count)+' to '+str(yes_count)+'.'
        tied = 'This statement\'s ruling is undecided. The vote was split '+str(yes_count)+' to '+str(no_count)+'.'
        default = 'No one voted (or something went wrong!). Boring.'
        
        if yes_count > no_count:
            return y_maj
        elif yes_count < no_count:
            return n_maj
        elif yes_count == no_count:
            return tied
        else:
            return default
        
    def flavor(self):
        event_string = 'LAST_CONTR'
        new_days, last_days = date_util.get_days_since(event_string)
        os.environ[event_string] =  str(new_days)
        days_since  = new_days - last_days
        a = '. Way to go, Torch! You have gone '+str(days_since)+' days without saying something controversial!'
        b = '. The \"days since Torch said something controversial\" counter has been reset.'
        
        