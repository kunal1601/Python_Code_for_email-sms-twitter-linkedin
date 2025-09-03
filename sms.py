from twilio.rest import Client

# Your Twilio credentials
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello Kunal, How are you. Tell me something about our project ",
    from_="+1 304 721 1950",   # Your Twilio phone number
    to="+9199830*****"     # Receiver's phone number (with country code)
)

print("Message sent! SID:", message.sid)
