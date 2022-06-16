import requests

def publishOnPage( pageId, pageAccessToken, imageUrl, caption ):

    request_url = "https://graph.facebook.com/"+ pageId +"/photos?url="+ imageUrl +"&message=" + caption + "&access_token="+ pageAccessToken
    print(request_url)
    data = requests.post(url = request_url)
    print(data)
    # return request_url