# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
"""
import os
import datetime

def get_days_since(event_string):
    now = datetime.datetime.today()
    now_delta = now - datetime.datetime.utcfromtimestamp(0)
    last = int(os.environ[event_string])
    return now_delta.days, last