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
		name = data['name']
		if state == "get_movie":
			db = dataset.connect('postgres://yraitcrdcotuhb:6c41e7f3055517601bffd7be8434801d2bb96234171828dc7f860432705b405d@ec2-107-20-224-137.compute-1.amazonaws.com:5432/d7fi5emvoirfqc')
			table = db['movie']
			movie = table.find(name=name)
			end = timeit.default_timer()
			return JsonResponse({
			'status': "ok",
			'text': f'{movie}',
			'time': runtime
		}, encoder=JSONEncoder)


	else:
		end = timeit.default_timer()
		return JsonResponse({
		'status': "ok",
		'text': "What do you expect to do?",
		'time': runtime
	}, encoder=JSONEncoder)