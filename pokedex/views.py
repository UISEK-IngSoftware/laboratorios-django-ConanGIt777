from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm
from django.shortcuts import redirect, render


def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers,
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
    pokemons = Pokemon.objects.filter(trainer=trainer)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer,
        'pokemons': pokemons
    }
    return HttpResponse(template.render(context, request))


def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})


def edit_trainer(request, trainer_id: int):
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})


def delete_trainer(request, trainer_id: int):
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('pokedex:index')


def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, pokemon_id: int):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})
def delete_pokemon(request, pokemon_id: int):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')
    