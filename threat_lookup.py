#!/usr/bin/env python3

"""
threat_lookup.py

Will allow user to input an IP, and will return the reputation of the IP
Author: Ahmed
"""

import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': '180.153.236.223',
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': 'Replace With Your Own API Key'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))