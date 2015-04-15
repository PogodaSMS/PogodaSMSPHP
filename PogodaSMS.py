from smsapi.client import SmsAPI
from smsapi.responses import ApiError

api = SmsAPI()

api.set_username('kbula@o2.pl')
api.set_password('smsapi')

#sending SMS
try:
	api.service('sms').action('send')

	api.set_content('Pogoda ok!')        
	api.set_to('668318524')
	api.set_from('ECO')

	result = api.execute()

	for r in result:
		print r.id, r.points, r.status

except ApiError, e:
	print '%s - %s' % (e.code, e.message)
	
	
