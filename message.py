from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class message:
    def __init__(self):
        account_sid = os.getenv('ACCOUNT_SID')
        auth_token = os.getenv('AUTH_TOKEN')
        self.client = Client(account_sid,auth_token)

    def message_decision(self,id_climate):
        number = input("Write your number (e.x.e +549xxxxxxxx)")
        if id_climate == 800:
            self.client.messages.create(
                body="Hey, What's up?\nThe ISS is available to see 🚀👨‍🚀",
                from_=f"whatsapp:{os.getenv('FROM_NUMBER')}",
                to=f"whatsapp:{number}"
            )
        else:
            self.client.messages.create(
                body="Hey, What's up?\nThe ISS is not available to see right now. Sorry 😥",
                from_=f"whatsapp:{os.getenv('FROM_NUMBER')}",
                to=f"whatsapp:{number}"
            )
