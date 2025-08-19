"""
Twilio SMS Script for NetBox.

This module provides a simple script that demonstrates how to send an SMS
message to a phone using the Twilio REST API. It uses environment variables
for Twilio credentials and phone numbers to keep secrets out of the code.
"""

import os
import requests
from extras.scripts import Script


class TwilioSMSScript(Script):
    class Meta:
        name = "Twilio SMS (Raw API)"

    def run(self, data, commit):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_FROM_NUMBER")
        to_number = os.getenv("TWILIO_TO_NUMBER")

        if not all([account_sid, auth_token, from_number, to_number]):
            self.log_failure("Missing one or more required Twilio "
                             "environment variables")
            return

        url = (
            f"https://api.twilio.com/2010-04-01"
            f"/Accounts/{account_sid}/Messages.json"
        )
        payload = {
            "From": from_number,
            "To": to_number,
            "Body": "Hello from NetBox 👋",
        }

        try:
            resp = requests.post(url, data=payload,
                                 auth=(account_sid, auth_token))
            if resp.status_code == 201:
                self.log_success(
                    f"Message sent successfully: SID {resp.json().get('sid')}")
            else:
                self.log_failure(
                    f"Twilio API error: {resp.status_code} {resp.text}")
        except Exception as e:
            self.log_failure(f"Exception: {e}")
