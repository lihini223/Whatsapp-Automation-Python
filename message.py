from twilio.rest import Client

account_sid = 'AC89d03492e78f7cf541223bf89a7bcacd'
auth_token = '6f7645afcea72ca7db3e0c02ea029121'
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='I need you so badly.❤',
        to='whatsapp:+0000000000'
    )

    print(message.sid)

