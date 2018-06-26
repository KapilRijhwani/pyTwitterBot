# Twitter bot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 'ktL61ssBdMOVwatvcXxNTm70a'
consumer_secret = 'bby0tPoQPuG1SJIGUYU7If2G5UvYjPqbYUSnJ9O3tz3AC623dq'
access_token = '1011536410845876225-WEE2JpCOyVlrcD6nt69JXhSrj5wRrW'
access_secret = 'xTkOyUKhizoDJ6a5de6rHngS8NqOqD6ndduIwQGtqL5zI'

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
