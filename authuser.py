import tweepy
import os
# From your app settings page
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")

consumer_secret = os.environ.get("CONSUMER_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth_url = auth.get_authorization_url()

print ('Please authorize: ' + auth_url)

verifier = input('PIN: ').strip()

auth.get_access_token(verifier)

print ("ACCESS_KEY = '%s'" % auth.access_token.key)
print ("ACCESS_SECRET = '%s'" % auth.access_token.secret)