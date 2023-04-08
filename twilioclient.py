import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = "ACf64d6b6529426f2e2c2d1e96bb925654"
auth_token = os.getenv('TWILIO_API_KEY')
cleint = Client(account_sid, auth_token)


def send_update(phone_number: str, message: str ):
    cleint.messages.create(
        to=phone_number,
        from_ = "+18337920631",
        body = message,
    )