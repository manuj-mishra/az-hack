import requests
from PIL import Image
from io import BytesIO

def getSummary(text):
    key = "1D69298B9E"
    endpoint = 'https://api.smmry.com/'

    data = {
        "sm_api_input":text
    }
    params = {
        "SM_API_KEY": key,
        "SM_LENGTH": "7"
    }
    headers = {"Expect":"100-continue"}
    response = requests.post(url=endpoint, params=params, data=data, headers=headers)
    content = response.json()['sm_api_content']
    return content
