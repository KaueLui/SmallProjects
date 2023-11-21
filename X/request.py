import tweepy
import time
import requests
from io import BytesIO
from PIL import Image

api = tweepy.Client(
    consumer_key = 'seu_consumer_key',
    consumer_secret = 'seu_consumer_secret',
    access_token = 'seu_access_token',
    access_token_secret = 'seu_access_token_secret'
)

def post_tweet_with_image(url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

hashtags = ["#goLOUD", "#LOUDWIN", "#LOUDgg"]

for hashtag in hashtags:
    images = api.search_images(hashtag)
    for image in images:
        post_tweet_with_image(image['url'], hashtag)
        time.sleep(10)  # Pausa por 10 segundos