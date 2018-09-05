from rest_framework.decorators import api_view
from rest_framework.response import Response
from recommender_app.ml_model.recommender import get_artist_recommendations


@api_view(['POST'])
def get_recommendation(request):
    data = request.data.dict()
    artist = data['artist']
    number = int(data['number'])
    response = dict(recommendations=get_artist_recommendations(artist, number))
    return Response(response)
