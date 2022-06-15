import requests

def publishOnPage( pageId, pageAccessToken, image_url, caption ):

    request_url = "https://graph.facebook.com/"+ pageId +"/photos?url="+ image_url +"&message=" + caption + "&access_token="+ pageAccessToken
    data = requests.post(url = request_url)
    print(request_url)
    # return request_url