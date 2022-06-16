import requests
import json 

def publishPost( userId, accessToken, imageUrl, caption ):

    # Making container
    request_url = "https://graph.facebook.com/v14.0/" + userId + "/media?image_url=" + imageUrl + "&caption="+ caption +"&access_token="+ accessToken
    print("Making Container...")
    data = requests.post(url = request_url)
    decoded_json = json.loads(data.text)
    print("Container created with id: ", decoded_json["id"])

    # Making post of container
    container_id = decoded_json["id"]
    request_url = "https://graph.facebook.com/v14.0/" + userId + "/media_publish?creation_id=" + container_id + "&access_token="+ accessToken
    print("Making Post...")
    data = requests.post(url = request_url)
    print("Post created: \n", data)
    