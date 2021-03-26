import requests
from PIL import Image
from io import BytesIO

def getImage(keyword):
    key = "AIzaSyBKbf_aR_m4i552iOuPAPb-VOJJkLn74yo"
    search_engine_id = "f980e922532fe1c1a"
    query = 'https://www.googleapis.com/customsearch/v1?' + 'key=' + key + '&cx=' + search_engine_id +'&q=' + keyword + '&searchType=image'
    response = requests.get(query)

    i = 0
    uri = ""
    while(not(uri.endswith(".jpg"))):
        uri = response.json()['items'][i]['link']
        i += 1
    
    print(uri)

    img_PIL = Image.open(requests.get(uri, stream=True).raw)
    return img_PIL