import os
import requests
import logging
from extras.scripts import Script

VERSION = "1.2"
print(f"Loaded TwilioNotify script v{VERSION}")
logger = logging.getLogger("netbox.scripts")
logger.info(f"TwilioNotify script v{VERSION} loaded")


class TwilioNotify(Script):
    class Meta:
        name = "Twilio SMS Notification"
        description = "Send an SMS via Twilio when an Event Rule triggers"

    def run(self, data, commit):
        obj = data  # in Event Rules, 'data' is already the dict
        obj_name = obj.get("display") or obj.get("name") or \
            f"ID {obj.get('id')}" or "Unknown"
        user = data.get("user") or "system"
        event = data.get("event") or "updated"

        import json
        print(f"DEBUG event payload: "
              f"{json.dumps(data, indent=2, default=str)}")

        # Try to extract useful fields
        obj_name = obj.get("name") or obj.get("display") or \
            f"ID {obj.get('id')}" or "Unknown"

        body = f"NetBox Event: Device '{obj_name}' was {event} by {user}"

        # Twilio creds from environment
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_FROM_NUMBER")
        to_number = os.getenv("TWILIO_TO_NUMBER")

        if not all([account_sid, auth_token, from_number, to_number]):
            self.log_failure("Missing Twilio environment variables")
            return

        url = (f"https://api.twilio.com"
               f"/2010-04-01/Accounts/{account_sid}/Messages.json")
        resp = requests.post(
            url,
            data={"From": from_number, "To": to_number, "Body": body},
            auth=(account_sid, auth_token),
            timeout=10,
        )

        if resp.status_code == 201:
            self.log_success(f"SMS sent: {body}")
        else:
            self.log_failure(f"Twilio API error "
                             f"{resp.status_code}: {resp.text}")
