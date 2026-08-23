#!/usr/bin/env python3

"""
threat_lookup.py

requirements: requests, 

Will allow user to input an IP, and will return the reputation of the IP
Author: Ahmed
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()
print(os.getenv('ABUSEIPDB_API_KEY'))

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

# This sets the parameters for the request
querystring = {
    'ipAddress': '180.153.236.223',
    'maxAgeInDays': '90'
}

# Header for the URL
headers = {
    'Accept': 'application/json',
    'Key': os.getenv('ABUSEIPDB_API_KEY')
}

# The code actually requesting the data from the resource (Abuse IPDB)
response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)

# Instructs how to display the data
def print_results(decodedResponse):
    print()
    print('***' * 5)
    print()
    print(f'Threat Report for IP: {decodedResponse['data']['ipAddress']}')
    print()

    print(f'IP: {decodedResponse['data']['ipAddress']}')
    print(f'Abuse Confidence Score: {decodedResponse['data']['abuseConfidenceScore']}')
    print(f'Country: {decodedResponse['data']['countryCode']}')
    print(f'Times Reported: {decodedResponse['data']['totalReports']}')
    print()

    print('***' * 5)

print_results(decodedResponse)