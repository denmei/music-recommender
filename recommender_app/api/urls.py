from django.conf.urls import url
from recommender_app.api.views import get_recommendation

urlpatterns = [
    url(r'^artist-recommendation$', get_recommendation, name='artist-recommendation-api'),
]