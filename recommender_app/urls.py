from django.conf.urls import url, include
from recommender_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recommendation/$', views.artist_prediction, name='predictartist'),
    url(r'^api/', include('recommender_app.api.urls'))
]