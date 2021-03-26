import requests
from PIL import Image
from io import BytesIO

def getImage(keyword):
    key = "AIzaSyBKbf_aR_m4i552iOuPAPb-VOJJkLn74yo"
    search_engine_id = "f980e922532fe1c1a"
    query = 'https://www.googleapis.com/customsearch/v1?' + 'key=' + key + '&cx=' + search_engine_id +'&q=' + keyword + "&searchType=image"
    response = requests.get(query)
    uri = response.json()['items'][0]['link']

    img_PIL = Image.open(requests.get(uri, stream=True).raw)
    img_PIL.save(keyword + "." + uri.split(".")[-1])

getImage("africa")