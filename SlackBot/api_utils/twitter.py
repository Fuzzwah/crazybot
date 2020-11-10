# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:21:45 2020

@author: Matt
"""

import tweepy
import os
import dotenv
from dotenv import load_dotenv

def main():
    load_dotenv()
    auth = tweepy.OAuthHandler(
        os.environ['TWITTER_API_KEY'], os.environ['TWITTER_SECRET_KEY'])
    auth.set_access_token(
        os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    
    api = tweepy.API(auth)
    tweets = api.user_timeline(os.environ['TWITTER_USER'])
    newest_tweet = most_recent_tweet(tweets)
    if newest_tweet != None:
        update_most_favorites(newest_tweet)
        reply = ("Very cool! Btw, congrats on "+
             str(newest_tweet.favorite_count)+
             " likes on your latest tweet! "+
             compare_to_most_favorites(newest_tweet))
    else:
        reply = 'It appears you deleted your Twitter. I am not sure how to respond to you now. Red peppers suck.'
    return reply

def most_recent_tweet(tweets):
    i=0
    while i<len(tweets):
        if tweets[i].retweeted:
            i+=1
        else:
            return tweets[i]
    return None

def update_most_favorites(tweet):
    most_recent_count = int(tweet.favorite_count)
    most_count = int(os.environ['MOST_FAVORITES'])
    if most_recent_count > most_count:
        dotenv.set_key(dotenv.find_dotenv(), 'MOST_FAVORITES', str(most_recent_count))
        return True
    return False

def compare_to_most_favorites(tweet):
    tweet_count = int(tweet.favorite_count)
    most_count = int(os.environ['MOST_FAVORITES'])
    if tweet_count > most_count:
        return "In fact, it's your personal best since I've been alive!"
    elif tweet_count == most_count:
        return "It must've been a very good tweet as it tied your personal best."
    else:
        return "Sadly it's nowhere near your best. Don't forget about growth mindset!"
