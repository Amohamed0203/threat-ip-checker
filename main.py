from dotenv import load_dotenv
import argparse

# Load variables from .env into the environment
load_dotenv()

from sources.abuseipdb import request_to_abuse_ipdb
from report import print_results
from utils import ip_validation

def request_from_user():
    # parser object
    parser = argparse.ArgumentParser(
    description = "This will collect the IP from the user"
    )

    # setting parameters for what is needed from user
    parser.add_argument("-i", "--ip", metavar = "ip", required = True, help = "Input and IP")

    args = parser.parse_args()

    return args.ip

requested_ip = str(request_from_user())

if ip_validation(requested_ip):
    decodedResponse = request_to_abuse_ipdb(requested_ip)
    if decodedResponse != None:
        print_results(decodedResponse)
else:
    print("IP format must be valid!")