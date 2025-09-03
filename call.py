from twilio.rest import Client

# Your Twilio credentials (find in Twilio Console → Account Info)
account_sid = "your_account_sid"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    twiml='<Response><Say voice="alice">Hello! This is a call from Python using Twilio. Have a great day!</Say></Response>',
    to="+9199830*****",     # Receiver’s phone number (with country code)
    from_="+9159039465"    # Your Twilio phone number
)

print("Call initiated! SID:", call.sid)
