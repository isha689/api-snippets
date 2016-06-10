# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "{{ account_sid }}"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

caller_id = client.caller_ids.get("PNe905d7e6b410746a0fb08c57e5a186f3")
print(caller_id.phone_number)