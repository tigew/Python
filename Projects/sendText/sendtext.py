from twilio.rest import Client

account_sid = "AC02d7e073b280ad3359ccfa3638e974fc"
auth_token = "78822077657e77eb6adf46bfb9c4a623"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+15302280677",
    from_="+15303534197",
    body="Test 2"
)
