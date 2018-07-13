from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from scrapyd_api import ScrapydAPI
from json import JSONEncoder
import timeit
import json
import dataset
from stuf import stuf

start = timeit.default_timer()
scrapyd = ScrapydAPI('https://myscrapyd.herokuapp.com/')

@csrf_exempt
def api(request):

	if request.method == 'POST':
		db = dataset.connect('postgresql://yraitcrdcotuhb:6c41e7f3055517601bffd7be8434801d2bb96234171828dc7f860432705b405d@ec2-107-20-224-137.compute-1.amazonaws.com:5432/d7fi5emvoirfqc')
		data = json.loads(request.body)
		state = data['state']
		name = data['name']
		#name = '%' + name + '%'

		if state == "search_movie":
			table = db['movie']
			sql = f"SELECT * FROM movie WHERE name = 'cameras'"
			results = db.query(sql)
			movies = []
			movie = {}
			for result in results:
			    movie['name'] = result['name']
			    movie['year'] = result['year']
			    movie['photo'] = result['photo']
			    movies.append(movie)
			end = timeit.default_timer()
			return JsonResponse({
			'status': "ok",
			'text': f'{movies}',
			'time': end - start
		}, encoder=JSONEncoder)

		if state == "get_movie":
			table = db['movie']
			sql = f'SELECT * FROM movie WHERE name LIKE "{name}" LIMIT 1'
			results = db.query(sql)
			movie = {}
			for result in results:
			    movie['name'] = result['name']
			    movie['year'] = result['year']
			    movie['photo'] = result['photo']
			    movie['link480'] = result['link480']
			    movie['link720'] = result['link720']
			    movie['link1080'] = result['link1080']
			return JsonResponse({
			'status': "ok",
			'text': f'{movie}',
			'text2': movie,
			'time': end - start
		}, encoder=JSONEncoder)


	else:
		end = timeit.default_timer()
		return JsonResponse({
		'status': "ok",
		'text': "What do you expect to do?",
		'time': end - start
	}, encoder=JSONEncoder)