import requests
from PIL import Image
from io import BytesIO

def getImage(keyword):
    key = "AIzaSyCHOFK7ECR2EU2qr112p5bJyvYIUR_kE38"
    search_engine_id = '2107b9a71ab149877'
    query = 'https://www.googleapis.com/customsearch/v1?' + 'key=' + key + '&cx=' + search_engine_id +'&q=' + keyword + "&searchType=image";
    response = requests.get(query)

    uri = response.json()['items'][0]['link']

    img_PIL = Image.open(requests.get(uri, stream=True).raw)
    img_PIL.save(keyword + "." + uri.split(".")[-1])