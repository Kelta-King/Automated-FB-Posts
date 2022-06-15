import requests
from Includes import config as conf
import json
from Actions import facebook as fb

start = 22
end = 30

x = requests.get(url = "https://picsum.photos/v2/list")
dt = json.loads(x.text)

i = start
while ( i <= end ):
    
    try:
        image_url = dt[i]['download_url']
        caption = "Image captured by " + dt[i]['author']
        i += 1

        fb.publishOnPage(conf.pageId, conf.pageAccessToken, image_url, caption)
        # print(dt)
    except Exception as e:
        print(e)
    

print("Total ", i-start, " posts made...")