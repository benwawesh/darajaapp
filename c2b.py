import requests
import important
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token


consumer_key = important.consumer_key
consumer_secret = important.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
         "ShortCode": important.shortcode ,
        "ResponseType": " Completed",
        "ConfirmationURL": "https://fullstackdjango.com/confirmation",
        "ValidationURL": "https://fullstackdjango.com/validation_url"}
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

register_url()

def simulate_c2b_transaction():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = { "ShortCode":important.shortcode,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn": important.test_msisdn,
        "BillRefNumber":"1223456" }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)
simulate_c2b_transaction()
