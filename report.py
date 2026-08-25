
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