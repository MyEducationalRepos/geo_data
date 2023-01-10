import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
import json
import os
import sys
from dotenv import load_dotenv
load_dotenv()


'''

Note that credentials are read from an .env file
This should be obtained from RapidAPI

'''

api_token = os.environ.get("RAPID_API_KEY")


url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"


headers = {
	"X-RapidAPI-Key": api_token,
	"X-RapidAPI-Host": "google-maps-geocoding.p.rapidapi.com"
}



'''
#If we have a list of addresses:

direcciones = ["14 Norte 221, Viña del Mar",
	"Chanchería Chile",
	"Plaza Sucre, Viña del Ma, Viña del Mar"]
    
for _, direccion in enumerate(direcciones):    
    querystring = {"address":direccion,"language":"es"}
    response = requests.request("GET", url, headers=headers, params=querystring)	
    print(response.text)
'''

# Just one address executed via terminal

if __name__ == "__main__" : 
	my_place = ' '.join([el.strip() for el in sys.argv[1:]])
	print(f"The place you are looking for is {my_place}\n")
	querystring = {"address":my_place,"language":"es"}
	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)


