# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
"""
import os
import datetime
import random
import pytz
from api_utils import twitter
from internal_utils import date_util as date
from chat_features import poll
import operator


def get_personal_message_reply(username):  
    switch={
        'bowser':'Shouldn\'t you be humiliating Yuca in smash?',
        'cactus':'Why are you at Chik-Fil-A at '+datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M")+'?',
        'chive':'I guess Quidditch didn\'t have a slack', 'cobra':'Send calf pics UwU',
        'ember':'Don\'t you have a trivia night to be hosting?', 'goji':'something something chess',
        'helix':'Isn\'t there a keg you should be tapping?', 'ice':'Oh so you have time to reply in chat?',
        'lotus':'Thanks for sharing! It has been at least '+
        lotus_last_reply()+' days since you last thought about Ring losing in semis.', 
        'magma':'Where\'s Swagtober 2: The Swaggening?',
        'momo':'Haha as if this will ever show', 'nova':'UwU',
        'onyx':'This is your automated monthly reminder to put your clothes back on.'+
        ' Reply \"LETMEBENUDE\" to cancel subscription.', 
        'pills': twitter.main(),
        'plank':'Ok gamer', 'puddles': 'TRUSTTTTTTTTTTTTTTT',
        'rex':'This isn\'t the #workouts channel', 'sabre':'Quick! Help get #YangGang2024 trending!',
        'skipper':'001110101011', 
        'tempo':'^He\'s speaking for the whole mod',
        'torch':'Don\'t you have controversy to go stir up elsewhere?', 'toro':'Okay, big meanie',
        'yoshi':'Haha as if this will ever show', 'yuca':'Very cool, Eugene!',
        'zorro':'Thank you for subscribing to LotusFacts! Your fact of the day is that it has been '+last_skied()+' days since you were last skied by Lotus! Congrats!'
    }
    default = "Wait a second... who are you??"
    return switch.get(username, default)

def get_personal_reaction_reply(username):
    switch={
        'bowser':'',
        'cactus':'',
        'chive':'', 'cobra':'',
        'ember':'', 'goji':'',
        'helix':'', 'ice':'',
        'lotus':'', 
        'magma':'',
        'momo':'', 'nova':'',
        'onyx':'', 
        'pills': '',
        'plank':'', 'puddles': '',
        'rex':'', 'sabre':'',
        'skipper':'', 
        'tempo':'',
        'torch': operator.methodcaller('torch_poll'), 'toro':'',
        'yoshi':'', 'yuca':'',
        'zorro':''
    }
    default = ""
    return switch.get(username, default)

def torch_poll(event):
    poll.BinaryVote(event, 'controversy', 10, 'angry', 'hugging_face')

def lotus_last_reply():
    event_string = 'LAST_MESSAGE'
    new_days, last_days = date.get_days_since(event_string)
    os.environ[event_string] = str(new_days)
    return str(new_days - last_days)

def last_skied():
    event_string = 'LAST_SKIED'
    new_days, last_days = date.get_days_since(event_string)
    return str(new_days - last_days)

def event_random():
    if random.uniform(0,1) <= 0.6:
        return True
    return False



