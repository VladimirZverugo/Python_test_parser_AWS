import requests
import json
import random

#HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
response = requests.get("https://data.covid19info.live/processeddata.js")
file = json.loads(response.text)

if response.status_code==200:

    regions = file['regions']
    country = regions[random.randint(0,len(regions)-1)]
    print(f"Country: {country[0]['en_name']} \nConfirmed COvid: {country[7][-1]['c']} \nRecovered: {country[7][-1]['r']}")

else:
    print("Error")
