# views.py
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from .forms import productions  
from .models import production
from django.db.models import Sum


def produite(request):
    # Vue pour ajouter de nouvelles ventes
    form = productions()  # Assurez-vous d'utiliser le nom correct du formulaire
    if request.method == 'POST':
        form = productions(request.POST)
        if form.is_valid():
            form.save()
            return redirect('production')

    context = {'form': form}
    return render(request, 'production/production.html', context)


def list_production(request):
    # Vue pour afficher la liste des ventes pour une date spécifique
  
    data = production.objects.all()
    context = {'data': data}
    return render(request, 'production/list.html', context)

def update(request, pk):
    # Vue pour mettre à jour une production spécifique
    produit = production.objects.get(id=pk)
    form = productions(instance=produit)
    if request.method == 'POST':
        form = productions(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('list_production')

    context = {'form': form}
    return render(request, 'production/production.html', context)

def remove(request, pk):
    # Vue pour supprimer une production spécifique
    data = production.objects.get(id=pk)
    data.delete()
    return redirect('list_production')

def recherche(request):
    # Vue pour effectuer une recherche parmi les productions
    donnée = production.objects.all()
    reshearch = request.GET.get('q')

    if reshearch:
        donnée = donnée.filter(date__icontains=reshearch)
        
        # Si des données sont trouvées après la recherche, rediriger vers la première date trouvé

    context = {'datap': donnée}
    return render(request, 'production/list.html', context)
