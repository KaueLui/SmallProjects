import tweepy
import time

api = tweepy.Client(
    consumer_key = 'seu_consumer_key',
    consumer_secret = 'seu_consumer_secret',
    access_token = 'seu_access_token',
    access_token_secret = 'seu_access_token_secret'
)

def post_tweet(text):
    try:
        tweet = api.create_tweet(text=text)
        print(tweet)
    except Exception as e:
        print(f"Erro ao postar tweet: {e}")

tweets = ["Hello, world!", "Olá, mundo!", "Hola, mundo!"]

for tweet in tweets:
    post_tweet(tweet)
    time.sleep(10)  # Pausa por 5 segundos
