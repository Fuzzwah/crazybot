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
    '''
    Dictionary functioning as switch/case statement,
    input users as keys and strings/functions returning strings
    as the value
    '''
 
    switch={
    }
    default = "Wait a second... who are you??"
    return switch.get(username, default)

def get_personal_reaction_reply(username):
    switch={
    }
    default = ""
    return switch.get(username, default)

#custom user reply functions can be added below, for now



