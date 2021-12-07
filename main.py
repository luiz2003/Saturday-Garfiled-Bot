#Get api keys from .env files
from dotenv import load_dotenv
load_dotenv()

import os

api_key = os.environ.get("API_KEY")
api_key_secret = os.environ.get("API_KEY_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

#import tweepy and set up the api
import tweepy

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#function that sends the tweet with image
def sendGarf():
    api.update_status_with_media("Saturday Baby", "saturdayGarf.png")

#schedule the tweets
import schedule
import time

schedule.every().saturday.at("10:00").do(sendGarf)

while True:
    schedule.run_pending()
    time.sleep(1)