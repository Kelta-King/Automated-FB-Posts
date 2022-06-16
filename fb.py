import requests
from Includes import config as conf
import json
from Actions import facebook as fb

start = 0
end = 100

x = requests.get(url = "https://picsum.photos/v2/list?page=3&limit=100")
dt = json.loads(x.text)

i = start
while ( i < end ):
    
    try:
        image_url = dt[i]['download_url']
        caption = "Image captured by " + dt[i]['author']
        i += 1
        fb.publishOnPage(conf.getPageId(), conf.getPageAccessToken(), image_url, caption)

    except Exception as e:
        print(e)
    

print("Total ", i-start, " posts made...")