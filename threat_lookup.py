#!/usr/bin/env python3

"""
threat_lookup.py

requirements: requests, 

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
    'Key': '01f32b88bbce4af7cb60c53d5fe02d3e42ff1911036e78386497c88b010871078c16d5e5a9d72405'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)

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