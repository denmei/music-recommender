from django.http import JsonResponse, HttpResponse
from recommender_app.ml_model.recommender import get_artist_recommendations
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def artist_prediction(request):
    """

    :param request: Must be a post-request that contains a parameter 'artist-name'
    :return: JSON with recommendations for the artist specified in 'artist-name'
    """
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        arguments = data.keys()
        if 'artist' in arguments and 'number' in arguments:
            input_artist = data["artist"]
            try:
                number = int(data["number"])
            except ValueError:
                response = dict(message='Number-argument is not a valid integer. Number was: %s.' % request.POST["number"])
                return JsonResponse(response, content_type='application/json', status=400)
            response = dict(recommendations=get_artist_recommendations(input_artist, number))
            return JsonResponse(response, content_type='application/json', status=200)
        else:
            response = dict(message='Missing argument. Required arguments are: artist, number.')
            return JsonResponse(response, content_type='application/json', status=400)
    else:
        response = dict(message='Must be a POST request.')
        return JsonResponse(response, content_type='application/json', status=400)


def index(request):
    """
    View for homepage
    :param request:
    :return:
    """
    return render(request, 'recommender_app/index.html')
