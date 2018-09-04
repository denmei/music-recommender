from django.conf.urls import url
from recommender_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recommendation/$', views.artist_prediction, name='predict-artist'),
]