from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+15302280677",
    from_="+15303534197",
    body="Test 2"
)
