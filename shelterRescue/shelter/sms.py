import pprint
import nexmo
import sys
from django.utils.functional import SimpleLazyObject

# Fill in API key and secret, and then comment out these lines:
print "WHOOPS! Please open sms.py and fill in your "
print "API key/secret and your Nexmo-purchased number"
print "Press Ctrl-C to quit and fill in the data."
sys.exit(1)

# ~~~ START: FILL IN BELOW ~~~
SENDER = "< purchase a new number from Nexmo and put it here>"
RECIPIENT = "< your cell phone number >"
_client = SimpleLazyObject(
	lambda: nexmo.Client(
		key="< FILL IN HERE >",
		secret="< FILL IN HERE >"))
# ~~~ END: FILL IN ABOVE ~~~


def send_sms(text, to, sender=SENDER):
	""" Send an SMS and return True on success """
	args = {
		'text': text,
		'to': to, 
		'from': sender,
	}

	print "Sending %r to %r from %r..." % (text, to, sender)
	response = _client.send_message(args)
	response = response['messages'][0]

	# fill in result
	result = dict(
		args=args,
		response=response,
	)
	if response['status'] == '0':
		result['success'] = True
		print 'Sent message', response['message-id']
		print 'Remaining balance is', response['remaining-balance']
	else:
		result['success'] = False
		print 'Error:', response['error-text']

	print 'Result', pprint.pformat(result)
	return result