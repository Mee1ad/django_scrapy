from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import JSONEncoder
import timeit

start = timeit.default_timer()

@csrf_exempt
def api(request):

    end = timeit.default_timer()
    runtime = end - start
    return JsonResponse({
        'status': 'ok',
        'text': "What do you expect to do?",
        'time': runtime
    }, encoder=JSONEncoder)