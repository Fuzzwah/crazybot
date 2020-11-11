# What is SlackBot?

This is a package for running a Bot on Slack as a Flask app. It is not a fully built codebase as it is currently in use in a highly personalized way.
In future updates, the functionality will shift to being more of a production deployment. 
**For now this code is just a starter framework to build a Slack bot with, for which you can customize functionality and easily add new modules**.  
</br>
  
# What does this code do?

## Handling Events as Threads
The [**event handling modules**](./event_handling) create a framework for 
processing all events in [**threads**](./event_handling/event_processor), pulled from an [**event queue**](./event_handling/event_queue).
This is necessary as the Slack API will duplicate any requests if it does not hear back within 3 seconds, 
and many events may require longer processsing time, thus it can be bypassed by passing all payloads to 
the [**event handler**](./event_handling/event_handler), allowing the bot to immediately respond HTTP 200 OK.

## Request and Response Wrapping
Some additional modules include [**models**](./models) for Slack events and replies. These are wrapper objects
that extend some extra functionality. In the case of [**replies**](./models/slack_reply), we can pass in a string or a
string returning function to get a reply unique to the user. There is a [**chat features**](./chat_features) module containing
a reaction based poll implementation, and more useful chat interactions in the future.  
</br>

# How can I run it?  

## Get Tokens
In order to have the bot run successfully on in a Slack workspace, you'll need to get access tokens
[**from registering your bot**](https://api.slack.com/apps) on the Slack API site (by clicking **Create New App**).


## Register Scopes
Once you have your **Bot User OAuth Access Token** (found in the **OAuth & Permissions** tab), **Client Secret**, and **Signing Secret**, 
be sure to add the required scopes from the **OAuth & Permissions** tab. The following scopes are needed for this app:

>channels:history  
>chat:write  
>reactions:read  
>users.profile:read  
>users:read  
>users:read.email  


## Add Tokens to .env
Next download this respository and open the **.env** file in a text editor where you will want to paste your 
access token, client secret, and signing secret into the **.env** file (without quotes):

    SLACK_TOKEN='your slack workspace token'
    SLACK_SS='your slack workspace signing secret'
    SLACK_CLIENT_SECRET='your slack client secret'

There are two more variables set aside for if you wish to work in a development worksapce for testing:

    SLACK_DEV_TOKEN=
    SLACK_DEV_SS=

You just need to register your app again on a new workspace.


## Setup Ngrok
Once the environment variables are set, go [**download ngrok**](https://ngrok.com/)
to run a URL tunnel to your local host domain. This allows for Slack workspace events to be received by your app.

Once it is downloaded, **run ngrok.exe** and enter:

    ngrok http 5000

This will open a URL that forwards to your local host. You can either copy the URL from the interface or open a webrower and go to:

    localhost:4040

From there copy the tunnel URL. This tab allows lets you see the live traffic of the URL which is useful for debugging.


## Register URL for Event Subcriptions
Next we need to register the URL with the Slack client so it forwards events to our local host.
Go to the specific page for your app [**from the Slack API site**](https://api.slack.com/apps). Click on the **Event Subscriptions** tab,
click **Enable Events**, and paste your URL into the **Request URL** box adding **"/slack/events"** to the end.

On the same page click the **Subscribe to bot events** button then click **Add Bot User Event** and add both the **message.channels** and **reaction_added**
events. 


## Run
Finally, run the **bot.py** file and make sure your **Request URL** is showing as verified. 

Nothing much will happen when events come in as it is personalizable (until abstracted in the future), but you can initiate this by editting the 
(**custom_reply.py**)[./internal_utils/custom_reply] classes: **get_personal_message_reply()** and **get_personal_reaction_reply()**, and adding to the dictionary
what responses you wish the bot to have for which users (denoted by display_name).

