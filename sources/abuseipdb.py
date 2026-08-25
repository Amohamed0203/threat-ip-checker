import os
import requests
import json

def request_to_abuse_ipdb(ip):
    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'

    # This sets the parameters for the request
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    # Header for the URL
    headers = {
        'Accept': 'application/json',
        'Key': os.getenv('ABUSEIPDB_API_KEY')
    }
    
    # The code actually requesting the data from the resource (Abuse IPDB)
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    if response.status_code == 401:
        print('\nAuthentication failed. Your API key is either missing, incorrect, or revoked.')
        return None
    elif response.status_code == 429:
        print('\nRate limit exceeded. Try again later.')
        return None
    elif response.status_code != 200:
        print(f'\nUnexpected error: HTTP {response.status_code}')
        return None


    # Formatted output
    decodedResponse = json.loads(response.text)

    return decodedResponse