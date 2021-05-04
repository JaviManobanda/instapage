from django.http import HttpResponse, JsonResponse  # * llama a una url
# utilities
from datetime import datetime
import json
"""Platzi views
    """


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello world {now}')


def sort_integers(request):
    numbers = list(map(lambda number: int(number),
                   request.GET['numbers'].split(',')))

    response = JsonResponse(
        {
            'hi': "Hello_worl",
            'numbers': sorted(numbers)
        },
        json_dumps_params={'indent': 4}
    )

    '''     import pdb
        pdb.set_trace()  # ? coloca en debugger en la consola  '''
    data = {
        'status': 'ok',
        'numbers': sorted(numbers),
        'description': 'Numbers sorted ok'
    }

    responsehttpJson = HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

    return responsehttpJson


def welcome(request, name, age):
    if age < 16:
        message = f'{name} you dont allowed here'
    else:
        message = f'Hello {name} Welcome'

    '''     import pdb
        pdb.set_trace() '''

    return HttpResponse(message)
