from django.http import JsonResponse
from recommender_app.ml_model.recommender import get_artist_recommendations


# Create your views here.
def artist_prediction(request):
    input_artist = request.POST["artist-name"]
    answer = {'recommendations': get_artist_recommendations(input_artist)}
    return JsonResponse(answer, content_type='application/json')
