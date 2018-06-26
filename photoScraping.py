# model scraping for bot

import requests
from bs4 import BeautifulSoup as bs
import os

image_tag = 'cricket'
url_tag = 'cricket'

# website with model images
url = 'https://www.pexels.com/search/' + url_tag + '/'

# download page for parsing
page = requests.get(url)

soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists(image_tag):
    os.makedirs(image_tag)

# move to new directory
os.chdir(image_tag)

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_tag + '-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
