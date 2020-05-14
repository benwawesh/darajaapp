import requests
from src.samples.access_token import generate_access_token
from src.samples.password import  password_generator
from src.samples import important
from src.samples.dateformat import  date_generator

access_token = generate_access_token()
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = {"Authorization": "Bearer %s" % access_token}
request = {
    "BusinessShortCode": important.business_shortCode,
    "Password": password_generator(),
    "Timestamp": date_generator(),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": important.partyA,
    "PartyB": important.business_shortCode,
    "PhoneNumber": important.partyA,
    "CallBackURL": "https://ancient-anchorage-87618.herokuapp.com/api/payments/lnm/",
    "AccountReference": "12345698",
    "TransactionDesc": "pay fees"
}

response = requests.post(api_url, json=request, headers=headers)

print(response.text)