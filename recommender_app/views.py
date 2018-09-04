from django.http import JsonResponse
from recommender_app.ml_model.recommender import get_artist_recommendations
from django.shortcuts import render
import json


def artist_prediction(request):
    """

    :param request: Must be a post-request that contains a parameter 'artist-name'
    :return: JSON with recommendations for the artist specified in 'artist-name'
    """
    if request.method == "POST":
        arguments = dict(request.POST).keys()
        if 'artist-name' in arguments and 'number' in arguments:
            input_artist = request.POST["artist-name"]
            try:
                number = int(request.POST["number"])
            except ValueError:
                response = dict(message='Number-argument is not a valid integer. Number was: %s.' % request.POST["number"])
                return JsonResponse(response, content_type='application/json', status=400)
            response = dict(recommendations=get_artist_recommendations(input_artist, number))
            return JsonResponse(response, content_type='application/json', status=200)
        else:
            response = dict(message='Missing argument. Required arguments are: artist-name, number.')
            return JsonResponse(response, content_type='application/json', status=400)


def index(request):
    """
    View for homepage
    :param request:
    :return:
    """
    return render(request, 'recommender_app/index.html')
