from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from scrapyd_api import ScrapydAPI
from json import JSONEncoder
import timeit
import json
import dataset

db = dataset.connect(
    'postgresql://yraitcrdcotuhb:6c41e7f3055517601bffd7be8434801d2bb96234171828dc7f860432705b405d@ec2-107-20-224-137.compute-1.amazonaws.com:5432/d7fi5emvoirfqc')


@csrf_exempt
def search_movie(request):
    data = json.loads(request.body)
    name = data['name']
    table = db['movie']
    sql = f"SELECT * FROM movie WHERE name LIKE '%{name}%'"
    results = db.query(sql)
    movies = []
    movie = {}
    for result in results:
        movie['name'] = result['name']
        movie['year'] = result['year']
        movie['photo'] = result['photo']
        movies.append(movie)
    return JsonResponse({
        'status': True,
        'text': movies,
    }, encoder=JSONEncoder)


@csrf_exempt
def get_movie(request):
    table = db['movie']
    sql = f'SELECT * FROM movie WHERE name LIKE "{name}" LIMIT 10'
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
        'status': True,
        'text': movie,
        'time': end - start
    }, encoder=JSONEncoder)
