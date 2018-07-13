from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from scrapyd_api import ScrapydAPI
from json import JSONEncoder
import timeit
import json

start = timeit.default_timer()
scrapyd = ScrapydAPI('https://myscrapyd.herokuapp.com/')

@csrf_exempt
def api(request):

	if request.method == 'POST':
		data = json.loads(request.body)
		state = data['state']
		if state == "find_all_movies":
			job = scrapyd.schedule('crawler', 'all_movies')

			end = timeit.default_timer()
			return JsonResponse({
			'status': "ok",
			'text': 'Job Submited /n You Can See Logs in Scrapyd or Gerapy',
			'time': runtime
		}, encoder=JSONEncoder)

	else:
		end = timeit.default_timer()
		return JsonResponse({
		'status': "ok",
		'text': "What do you expect to do?",
		'time': runtime
	}, encoder=JSONEncoder)