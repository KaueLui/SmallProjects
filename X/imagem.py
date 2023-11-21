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

# Lista de tweets programados com imagens
tweets_programados = [
    {"texto": "Olá, mundo!", "imagem": "caminho/para/sua/imagem1.jpg"},
    {"texto": "Bom dia!", "imagem": "caminho/para/sua/imagem2.jpg"},
    {"texto": "Boa tarde!", "imagem": "caminho/para/sua/imagem3.jpg"},
    {"texto": "Boa noite!", "imagem": "caminho/para/sua/imagem4.jpg"},
]

# Enviar tweets programados com intervalo de 1 hora
for tweet in tweets_programados:
    # Primeiro, carregamos a imagem
    media = api.media_upload(tweet["imagem"])
    
    # Em seguida, enviamos o tweet com a imagem
    api.update_status(status=tweet["texto"], media_ids=[media.media_id])
    
    time.sleep(3600)  # Espera por 1 hora (3600 segundos)
