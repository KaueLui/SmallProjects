import tweepy
import time


api = tweepy.Client(
    
    consumer_key="",
    consumer_secret="",
    bearer_token="",
    access_token="",
    access_token_secret=""
)

def post_tweet(text):
    try:
        tweet = api.create_tweet(text=text)
        print(tweet)
    except Exception as e:
        print(f"Error posting tweet: {e}")


post_tweet("Hello, worlds!")