import os
import requests
import json

def request_to_grey_noise(ip):
    url = f'https://api.greynoise.io/v3/community/{str(ip)}'

    response = requests.request("GET", url)

    if response.status_code == 429:
        print('\nNotice:\nRate limit exceeded for Grey Noise.')
        return None
    elif response.status_code == 404:
        return json.loads(response.text)
    elif response.status_code != 200:
        print(f'\nUnexpected error from Grey Noise: HTTP {response.status_code}')
        return None
    
    grey_noise_response = json.loads(response.text)

    return grey_noise_response