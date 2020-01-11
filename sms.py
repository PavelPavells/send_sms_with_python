from twilio.rest import Client 
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_ = '+79585692313',
    body = 'I CANT BELIEVE THIS WORKS.',
    to = '+79200851059'
)
print(message.sid)