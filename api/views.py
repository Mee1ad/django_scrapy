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
		movie = data['movie']
		category = data['category']
		job = scrapyd.schedule('crawler', 'search', category=f"{category}", movieName=f"{movie}")
		while(scrapyd.job_status('crawler', job) == 'pending'):
			print("Pending")
			time.sleep(.5)
			print("Continue")
			continue
		else:
			 print("Complete")

		end = timeit.default_timer()
		return JsonResponse({
		'status': "ok",
		'text': job,
		'time': runtime
	}, encoder=JSONEncoder)

	else:
		end = timeit.default_timer()
		return JsonResponse({
		'status': "ok",
		'text': "What do you expect to do?",
		'time': runtime
	}, encoder=JSONEncoder)