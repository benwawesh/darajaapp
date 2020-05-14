import requests
from requests.auth import HTTPBasicAuth
import important


def generate_access_token():
    consumer_key = important.consumer_key
    consumer_secret = important.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    print (r.json())
    json_response =r.json()
    my_access_token=json_response['access_token']

    return my_access_token
print(generate_access_token())