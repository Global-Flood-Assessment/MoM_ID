# code to test google flood API
"""
This script tests the Google Flood API by retrieving flood gauges for a specified region.

Functions:
    None

Usage:
    1. Ensure you have a `.env` file in the same directory with a valid API key under the key `KEY`.
    2. Run the script to print the number of flood gauges in the specified region.

Dependencies:
    - dotenv: To load environment variables from a `.env` file.
    - requests: To make HTTP requests to the Google Flood API.

Environment Variables:
    - KEY: Your Google Flood API key.

Constants:
    - region_code: The code of the region for which to retrieve flood gauges (default is "ID" for Indonesia).

API Endpoint:
    - https://floodforecasting.googleapis.com/v1/gauges:searchGaugesByArea

Example:
    $ python googleflood_test.py
"""

from dotenv import dotenv_values
import requests

# get API key
config = dotenv_values(".env")
KEY = config["KEY"]

# set up a region
region_code = "ID"

# get gauges by region
res = requests.post(
    f"https://floodforecasting.googleapis.com/v1/gauges:searchGaugesByArea?key={KEY}",
    json={"regionCode": region_code},
).json()
gauges = res["gauges"] if res else []

print(len(gauges))
