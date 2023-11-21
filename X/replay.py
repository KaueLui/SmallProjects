import tweepy
import time

api = tweepy.Client(
    consumer_key = '4z21w0WobIximyFpZJrMbvNMj',
    consumer_secret = '3H5K5W5BRTdbGyeV0lFfXvNeCGuWT5l5PaPypdJtNvTnOGeZrR',
    access_token = '1486140273226924038-d5XiPzp3WQwMsv1dN5dAQbH0KVs6uw',
    access_token_secret = '1QToCmijU3up97huhrZrjzQScwJg1ysVIdu06mknmVaLT'
)

def post_tweet(text):
    try:
        tweet = api.create_tweet(text=text)
        print(tweet)
    except Exception as e:
        print(f"Erro ao postar tweet: {e}")

def retweet_with_hashtag(hashtag):
    try:
        tweets = api.search_all_tweets(query=hashtag, tweet_mode='extended', lang='pt', count=10)
        for tweet in tweets:
            api.retweet(id=tweet.id)
            print(f"Retuitado: {tweet.full_text}")
            time.sleep(60000)  # Pausa por 10 segundos
    except Exception as e:
        print(f"Erro ao retuitar: {e}")

# tweets = ["Hello, world!", "Olá, mundo!", "Hola, mundo!"]
tweets = ["Hello, world!", "Olá, mundo!"]

for tweet in tweets:
    post_tweet(tweet)
    time.sleep(10)  # Pausa por 10 segundos

retweet_with_hashtag("#goLOUD")
