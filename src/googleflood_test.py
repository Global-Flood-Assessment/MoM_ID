# code to test google flood API

from dotenv import dotenv_values
import requests

# get API key
config = dotenv_values(".env")
KEY = config['KEY']

# set up a region
region_code = "ID"

# get gauges by region
res = requests.post(
    f'https://floodforecasting.googleapis.com/v1/gauges:searchGaugesByArea?key={KEY}',
    json={'regionCode': region_code},
).json()
gauges = res['gauges'] if res else []

print(len(gauges))
