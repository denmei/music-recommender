from django.contrib import admin
from recommender_app.models import Artist

# Register your models here.

myModels = [Artist]
admin.site.register(myModels)
