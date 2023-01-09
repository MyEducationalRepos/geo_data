import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
load_dotenv()



'''

Note that credentials are read from an .env file
This should be obtained from RapidAPI

'''


api_token = os.environ.get("RAPID_API_KEY")

import requests

url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

#A case

querystring = {"address":"14 Norte 821, Viña Del Mar","language":"es"}

headers = {
	"X-RapidAPI-Key": api_token,
	"X-RapidAPI-Host": "google-maps-geocoding.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
