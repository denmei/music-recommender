from django.contrib import admin
from recommender.models import Artist

# Register your models here.

myModels = [Artist]
admin.site.register(myModels)
