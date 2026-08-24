# Threat IP Checker

A Python CLI tool that checks IP addresses against AbuseIPDB to flag known malicious or abusive activity.

## Features

- Validates IP address format before making any API calls
- Queries the AbuseIPDB API for real-time IP reputation data
- Displays abuse confidence score, country, and total reports for a given IP

## Requirements

- Python 3.12 or higher
- A free [AbuseIPDB](https://www.abuseipdb.com/) account and API key
- `requests` and `python-dotenv` libraries

## Setup

1. Clone the repository
2. Install dependencies:
```bash
   pip install requests python-dotenv
```
3. Create a `.env` file in the project root and add your API key:
```
   ABUSEIPDB_API_KEY=your_api_key_here
```

## How to Run

```bash
python threat_lookup.py -i <ip_address>
```

**Example:**

```bash
python threat_lookup.py -i 8.8.8.8
```

**Sample output:**

```
***************

Threat Report for IP: 8.8.8.8

IP: 8.8.8.8
Abuse Confidence Score: 0
Country: US
Times Reported: 0

***************
```

## Project Structure

- `ip_validation` — checks that the provided input is a properly formatted IP address
- `request_from_user` — handles CLI argument parsing
- `request_to_abuse_ipdb` — sends the request to the AbuseIPDB API and returns the parsed response
- `print_results` — formats and displays the threat report

## Notes

This project was built to practice working with external APIs, environment variables, and JSON parsing in Python.