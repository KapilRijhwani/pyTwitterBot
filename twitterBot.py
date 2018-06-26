# Twitter bot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

image_tag = 'cricket'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir(image_tag)

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    print(model_image)
    api.update_with_media(model_image)
    time.sleep(60)
