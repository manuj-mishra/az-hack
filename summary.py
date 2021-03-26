import requests
from PIL import Image
from io import BytesIO

def getSummary(text):
    key = "1D69298B9E"
    sm_len = 7
    query = 'https://api.smmry.com/' + '&SM_API_KEY=' + key +'&SM_LENGTH=' + str(sm_len)
    response = requests.get(query)
    print(response.json())
    # content = response.json()['sm_api_content']
    # return content
