import pprint
import nexmo
from django.utils.functional import SimpleLazyObject

SENDER = "12016728857"
HENRY = "12123350455"
JADE = "16282208811"
JOHN = "16502782948"

_client = SimpleLazyObject(
	lambda: nexmo.Client(
		key="f90c82e2",
		secret="bf515501babcffd4"))

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