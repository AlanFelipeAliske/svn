import os
from twilio.rest import Client

account_sid = os.environ.get('AC2881f4f1ee65dbc8cb0813f93c0ce870')
auth_token = os.environ.get('9150335b55fe250daa2605964a50f695')

client = Client(account_sid, auth_token)    

client.messages.create(from_=os.environ.get('+18593281191'),
                       to=os.environ.get('+55 41 99530 9999 '),
                       body='Você enviou um SMS em Python usando o Twilio!')

