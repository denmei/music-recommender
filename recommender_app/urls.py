from django.conf.urls import url
from recommender_app import views

urlpatterns = [
    url(r'^recommendation/$', views.artist_prediction, name='predict-artist'),
]