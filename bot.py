#!/home/ethiopiagoogling/tweetbot/venv/bin/python
# -*- coding: utf-8 -*-
import tweepy
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import date
load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

access_token=os.environ.get("ACCESS_TOKEN")
access_token_key=os.environ.get("ACCESS_TOKEN_SECRET")
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_key)

# Create API object
api = tweepy.API(auth)

sheet_url = os.environ.get("TREND_DATA_ENDPOINT")
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df=pd.read_csv(url_1)
today = str(date.today())
result = df[ (df['Date'] == today )]
topic=result.Topic.to_list()
query=result.Query.to_list()
if topic or query:
    trending="Rising Topic: "+topic[0]+", \nRising Query: "+query[0]
    api.update_status(trending)
