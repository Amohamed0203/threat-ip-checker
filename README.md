# Threat IP Checker

A Python CLI tool that checks IP addresses against multiple threat intelligence sources — AbuseIPDB and GreyNoise — to flag known malicious or abusive activity and distinguish targeted threats from internet-wide background noise.

## Features

- Validates IP address format before making any API calls
- Queries the AbuseIPDB API for real-time IP reputation data (abuse score, country, report count)
- Queries the GreyNoise Community API to determine whether an IP is:
  - A known legitimate business service (e.g. Google DNS, Cloudflare)
  - Part of internet-wide mass scanning (benign or malicious)
  - Not observed at all — a signal that activity may be targeted rather than opportunistic
- Detects and reports API errors (invalid/missing key, rate limiting, etc.) instead of crashing
- Modular design — each API source is isolated in its own file for easy testing and extension

## Requirements

- Python 3.12 or higher
- A free [AbuseIPDB](https://www.abuseipdb.com/) account and API key
- `requests` and `python-dotenv` libraries

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Make a `.env` file in the project root and add your API key

## How to Run

```bash
python main.py -i <ip_address>
```

**Example:**

```bash
python main.py -i 8.8.8.8
```

## Notes

This project was built to practice working with external APIs, environment variables, JSON parsing, and multi-source data correlation in Python. It's an evolving project — started as a single-source CLI tool and is being extended into a multi-source threat intelligence correlator with AI-assisted analysis.