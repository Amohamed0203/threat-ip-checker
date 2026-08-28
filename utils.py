import ipaddress

def ip_validation(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False