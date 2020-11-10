# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
@purpose: base for Bot
"""

import slack_sdk
import os
from dotenv import load_dotenv
from flask import Flask, Response
from slackeventsapi import SlackEventAdapter
from event_handling import slack_event_handler

load_dotenv()

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SLACK_DEV_SS'], '/slack/events', app)

token = os.environ['SLACK_DEV_TOKEN']
client = slack_sdk.WebClient(token=token)
bot_id = client.api_call('auth.test')['user_id']
event_handler = slack_event_handler.EventHandler(client)

@slack_event_adapter.on('reaction_added')
@slack_event_adapter.on('message')
def event_listener(payload):
    '''
    Passes event payload onto event handler,
    returns 200 OK to server. This framework is 
    sadly necessary as Slack will resend messages if the 
    response code is still processing after 3 seconds.
    '''
    event_handler.handle(payload)
    return Response(status=200)

if __name__ == "__main__":
    app.run(debug=False)
    
