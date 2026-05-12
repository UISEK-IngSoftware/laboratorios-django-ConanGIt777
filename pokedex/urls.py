from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static imort static 
from lab8 import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)