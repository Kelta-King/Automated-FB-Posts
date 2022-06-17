import requests
from Includes import config as conf
import json
from Actions import instagram as ig

from google_images_download import google_images_download   #importing the library
from essential_generators import DocumentGenerator
gen = DocumentGenerator()
response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"cricket","limit":3,"no_download": True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function

images_paths = []
for k, v in paths[0].items():
    images_paths += v

for x in images_paths:
    image_url = x
    caption = gen.sentence()
    ig.publishPost( conf.getUserId(), conf.getAccessToken(), image_url, caption )

# for x in images_paths:
#     try:
#         image_url = x
#         caption = "sample image captions!"
#         ig.publishPost( conf.getUserId(), conf.getAccessToken(), image_url, caption )
#     expect:
#         print(dp.text)