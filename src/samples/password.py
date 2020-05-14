import base64
from src.samples.dateformat import date_generator
from src.samples import important


def password_generator():
    date = date_generator()
    data_to_encode = important.business_shortCode + important.lipa_na_mpesa_passkey + date
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8')
    return decoded_password