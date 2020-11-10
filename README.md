# SlackBot

This code is a framework for running a Bot on Slack as a Flask app.
The [event handling modules](SlackBot/event_handling) create a framework for 
processing all events in [threads](SlackBot/event_handling/event_processor), pulled from an [event queue](SlackBot/event_handling/event_queue).
This is necessary as the Slack API will duplicate any requests if it does not hear back within 3 seconds, 
and many events may require longer processsing time, thus it can be bypassed by passing all payloads to 
the [event handler](SlackBot/event_handling/event_handler), allowing the bot immediately respond HTTP 200 OK.

Some additional modules include [models](SlackBot/models) for Slack events and replies. These are information wrappers
that extend some extra functionality. In the case of [replies](SlackBot/models/slack_reply), we can pass in a string or a
string returning function to get a reply unique to the user. There is a [chat features](SlackBot/chat_features) module containing
a reaction based poll implementation that will count reactions to determine the results. It can take any two reactions as input, 
as well as a poll duration.
