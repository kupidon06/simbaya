# views.py
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from .forms import seller  # Assurez-vous d'utiliser le nom correct du formulaire
from .models import sell
from django.db.models import Sum
from depenses.models import spend
from production.models import production

def ventes(request):
    # Vue pour ajouter de nouvelles ventes
    form = seller()  # Assurez-vous d'utiliser le nom correct du formulaire
    if request.method == 'POST':
        form = seller(request.POST)
        if form.is_valid():
            form.save()
            
            
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/vente.html', context)


def fichier(request, pk):
    global datau
    datau = spend.objects.filter(date=pk)
    data = sell.objects.filter(date=pk)
    prod=production.objects.filter(date=pk)
    
    
    total_vente_for_date = data.aggregate(total_vente=Sum('Somme_gnf'))['total_vente']
    #-----------------------------------------------------------------------------------------------
   
    total_depense_for_date = datau.aggregate(total_depense=Sum('Somme_gnf'))['total_depense']
    #-------------------------------------------------------------------------------------
  
    if prod.first().produit !=None and prod.first().initiale != None and prod.first().usine !=None:

        production_day=prod.first().produit
        initial_day=prod.first().initiale
        usine_day=prod.first().usine
    else:
        production_day=0
        initial_day=0
        usine_day=0


        

  


    if total_depense_for_date !=None:
        totals=total_vente_for_date-total_depense_for_date
    else:
        totals=total_vente_for_date
    
    total_sortie=sell.objects.filter(date=pk).aggregate(Sum('sortie'))['sortie__sum']
    total_ventes=sell.objects.filter(date=pk).aggregate(Sum('vente'))['vente__sum']
    total_vendu=sell.objects.filter(date=pk).aggregate(Sum('vendu'))['vendu__sum']
    total_retour=sell.objects.filter(date=pk).aggregate(Sum('retourner'))['retourner__sum']
    total_credit=sell.objects.filter(date=pk).aggregate(Sum('credit'))['credit__sum']
    #-------------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------------------
    date=data.first().date

    data = sell.objects.filter(date=pk)
    context = {'datap': data,'total':totals,'total_depense':total_depense_for_date,'total_vente':total_vente_for_date,'datau':datau,'total_ventes':total_ventes,
    'date':date,'total_retour':total_retour,'production':production_day,'total_credit':total_credit,'total_vendu':total_vendu,'total_sortie':total_sortie,'initial':initial_day,'usine':usine_day}
    return render(request, 'vente/print.html', context)

    # Création d'un classeur Excel et d'une feuille
    
    


    return response

def list_vente(request, pk):
    # Vue pour afficher la liste des ventes pour une date spécifique
    global datau
    datau = sell.objects.filter(date=pk)
    data = sell.objects.filter(date=pk)
    datau = datau.first().date
    recapitulatif = sell.objects.values('date').annotate(total_vente=Sum('Somme_gnf'))
    total_vente_for_date = data.aggregate(total_vente=Sum('Somme_gnf'))['total_vente']
    
    context = {'datap': data, 'datau': datau,'vente':recapitulatif}
    return render(request, 'vente/list.html', context)

def update(request, pk):
    # Vue pour mettre à jour une vente spécifique
    vendu = sell.objects.get(id=pk)
    form = seller(instance=vendu)
    if request.method == 'POST':
        form = seller(request.POST, instance=vendu)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/vente.html', context)

def remove(request, pk):
    # Vue pour supprimer une vente spécifique
    data = sell.objects.get(id=pk)
    data.delete()
    return redirect('list_jours')

def recherche(request):
    # Vue pour effectuer une recherche parmi les ventes
    donnée = sell.objects.all()
    reshearch = request.GET.get('q')

    if reshearch:
        donnée = donnée.filter(date__icontains=reshearch)
        
        # Si des données sont trouvées après la recherche, rediriger vers la première date trouvée
        if donnée.exists():
            datau = donnée.first().date
            url = reverse('list_vente', kwargs={'pk': datau})
            return redirect(url)

    context = {'datap': donnée}
    return render(request, 'vente/list.html', context)

def tableau_recapitulatif(request):
    # Vue pour afficher un tableau récapitulatif des ventes par jour
    recapitulatif = sell.objects.values('date').annotate(total_vente=Sum('Somme_gnf')).order_by('-date')
    context = {'datap': recapitulatif}
    return render(request, 'vente/day.html', context)

def list_credit(request, pk):
    # Vue pour afficher la liste des ventes à crédit pour un véhicule spécifique
    data = sell.objects.filter(Vehicule=pk)
    context = {'datap': data}
    return render(request, 'credit/list.html', context)

def credit(request):
    # Vue pour afficher la page de gestion des crédits
    recapitulatif = sell.objects.values('Vehicule').annotate(total_vente=Sum('credit'))
    context = {'datap': recapitulatif}
    return render(request, 'credit/credit.html', context)

def cref(request, pk):
    # Vue pour mettre à jour le statut de crédit pour une vente spécifique
    # Fetch the sell object by its primary key
    vendu = sell.objects.get(id=pk)

    # Update the credit_status field
    vendu.statut_credit = 'payé'  # Update this based on your actual credit_status values

    # Save the changes
    vendu.save()

    # Redirect to the 'credit' page
    return redirect('credit')
