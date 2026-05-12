from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
        }, 
        request))

def pokemon(request, pokemon_id: int):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))
def trainer_details(request, trainer_id: int):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))