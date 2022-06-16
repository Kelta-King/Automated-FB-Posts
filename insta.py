import requests
from Includes import config as conf
import json
from Actions import instagram as ig

image_url = "https://cdn.ilovefreesoftware.com/wp-content/uploads/2018/01/Bulk-Encode-URL-Online-with-these-4-Free-Websites.jpg"
caption = "sample image"

ig.publishPost( conf.getUserId(), conf.getAccessToken(), image_url, caption )
