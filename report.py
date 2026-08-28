# Instructs how to display the data

def message_for_grey_noise(grey_noise_response):
    ip = grey_noise_response['ip']

    if grey_noise_response.get('riot'):
        name = grey_noise_response.get('name', 'a known service')
        return (f'{ip} belongs to {name}, a known legitimate business service — likely safe.')

    elif grey_noise_response.get('noise'):
        classification = grey_noise_response.get('classification')
        if classification == 'malicious':
            return (f'{ip} has been observed mass-scanning the internet for malicious purposes — likely opportunistic, not targeted at you specifically.')
        elif classification == 'benign':
            return (f'{ip} has been observed mass-scanning the internet and is classified as benign (e.g. a known research scanner).')
        else:
            return (f'{ip} has been observed mass-scanning the internet, but its classification is unknown.')

    else:
        return (f'{ip} has not been observed scanning the internet or found in known business services — this may indicate targeted activity. Investigate further.')


def print_results(abuse_ipdb_response, grey_noise_response):
    print()
    print('***' * 5)
    print()
    print(f'Threat Report for IP: {abuse_ipdb_response['data']['ipAddress']}')
    print('-' * len(f'Threat Report for IP: {abuse_ipdb_response['data']['ipAddress']}'))
    print()

    print(f'IP: {abuse_ipdb_response['data']['ipAddress']}')
    print(f'Abuse Confidence Score: {abuse_ipdb_response['data']['abuseConfidenceScore']}')
    print(f'Country: {abuse_ipdb_response['data']['countryCode']}')
    print(f'Times Reported: {abuse_ipdb_response['data']['totalReports']}')
    print()


    if grey_noise_response != None:
        print()
        print('Message from GreyNoise:')
        print('-' * len('Message from GreyNoise:'))
        print()
        print(message_for_grey_noise(grey_noise_response))
        print()

    print('***' * 5)