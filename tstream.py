import json
import tweepy

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

API_KEY = 'vHMWRlc7GSiVEDooO1ytsvEzfm122bfO7RKImjhmBJwVChHq5P'
API_SECRET_KEY = 'vHMWRlc7GSiVEDooO1ytsvEzfm122bfO7RKImjhmBJwVChHq5P'
ACCESS_TOKEN = '1270088779592843266-jOhP79V7XKXVaCayiScmnl7Z4XPfiO'
ACCESS_SECRET = 'q07q0XTxO3bflSdovzS5RC9APMtIoKXwhoUcvvkr4GGmc'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


class Listener(tweepy.Stream):
    def on_status(self, status):
        print(status.id)

stream_tweet = Listener(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
stream_tweet.filter(track=["Tweepy"])
