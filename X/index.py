import tweepy
import time

# Autenticação na API do Twitter

consumer_key = 'seu_consumer_key'
consumer_secret = 'seu_consumer_secret'
access_token = 'seu_access_token'
access_token_secret = 'seu_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Lista de tweets programados
tweets_programados = ["Olá, mundo!", "Bom dia!"]

# Enviar tweets programados com intervalo de 1 hora
for tweet in tweets_programados:
    api.update_status(tweet)
    time.sleep(10000)  # Espera por 1 hora (3600 segundos)
