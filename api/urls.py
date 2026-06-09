from django.urls import path, include
from rest_framework import routers
from .views import PokemonViewSet, trainerViewSet

router = routers.DefaultRouter()
router.register(r'pokemons', PokemonViewSet)
router.register(r'trainers', trainerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
