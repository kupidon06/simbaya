from django.shortcuts import render
from vente.models import sell
from django.utils import timezone
from django.db.models import Sum, Avg
from production.models import production
from depenses.models import spend
from matiere.models import Matiere

def ventes_mois_en_cours(request):
    mois_en_cours = timezone.now().month
    annee_en_cours = timezone.now().year

    ventes_mois_en_cours = sell.objects.filter(
        date__month=mois_en_cours,
        date__year=annee_en_cours
    ).values('Vehicule').annotate(total_ventes=Sum('vendu')) 
    # --------------------------graphe rentabilité----------------------------
    rentabilité =production.objects.filter(
        date__month=mois_en_cours,
        date__year=annee_en_cours).values('date').annotate(renta=Avg('rentabilité')) 
    renta=production.objects.filter(
        date__month=mois_en_cours,
        date__year=annee_en_cours).values('date').aggregate(hyp=Avg('rentabilité'))['hyp'] or 0

    # ----------------------------"rapport--------------------
    vente = sell.objects.filter(
        date__month=mois_en_cours,
        date__year=annee_en_cours
    ).aggregate(vente=Sum('Somme_gnf'))['vente'] or 0

    depensé = spend.objects.filter(
        date__month=mois_en_cours,
        date__year=annee_en_cours
    ).aggregate(depensé=Sum('Somme_gnf'))['depensé'] or 0
    stock_e=Matiere.objects.all().last().stock_emballage or 0
    stock_r=Matiere.objects.all().last().stock_rouleaux or 0

    return render(request, 'home/home.html', {'ventes_par_voiture': ventes_mois_en_cours,'renta':renta, 'rentabilite': rentabilité, 'vente': vente, 'depensé': depensé, 'rapport': vente - depensé,'stock_r':stock_r,'stock_e':stock_e})


def rap(request):
    

    # Pour ce mois
    recapitulatif = sell.objects.values('date__month').annotate(total_vente=Sum('Somme_gnf')).order_by('-date__month') 
    recap_depenses = spend.objects.values('date__month').annotate(total_depense=Sum('Somme_gnf')).order_by('-date__month') 

    # Créer un dictionnaire pour stocker la différence entre les ventes et les dépenses pour chaque mois
    resultats = {}
    for vente in recapitulatif:
        mois = vente['date__month'] or 0
        montant_vente = vente['total_vente'] or 0

        # Trouver la dépense correspondante pour le même mois
        depense = next((dep for dep in recap_depenses if dep['date__month'] == mois), None)

        # Calculer la différence (vente - dépense) et stocker dans le dictionnaire
        if depense:
            montant_depense = depense['total_depense']
            difference = montant_vente - montant_depense
            resultats[mois] = difference
        else:
            difference = montant_vente - 0
            resultats[mois] = difference
        
        
       

    context = {'resultats': resultats}
    return render(request, 'home/rapport.html', context)


def details(request, pk):
    mois_vente = sell.objects.filter(date__month=pk)
    mois_depense = spend.objects.filter(date__month=pk)

    
    recapitulatif_vente = mois_vente.values('date').annotate(total_vente=Sum('Somme_gnf')).order_by('date')
    recapitulatif_depense = mois_depense.values('date').annotate(total_depense=Sum('Somme_gnf')).order_by('date')
    somme_vente=recapitulatif_vente.aggregate(total_vente_mois=Sum('total_vente'))['total_vente_mois']

    somme_depense=recapitulatif_depense.aggregate(total_depense_mois=Sum('total_depense'))['total_depense_mois'] or 0
    benefice=somme_vente-somme_depense or 0

    context = {'vente': recapitulatif_vente, 'depenses': recapitulatif_depense,'mois_vente':somme_vente,'mois_depense':somme_depense,'benef':benefice}
    return render(request, 'home/details.html', context)
def recherche(request):
    # Filtrer les ventes et les dépenses pour le mois donné
    mois_vente = sell.objects.all()  # You may need to adjust this query based on your needs
    mois_depense = spend.objects.all()  # Similarly, adjust this query

    # Vue pour effectuer une recherche parmi les ventes
    ventes_par_mois = mois_vente.values('date').annotate(total_vente=Sum('Somme_gnf')).order_by('date')
    depenses_par_mois = mois_depense.values('date').annotate(total_depense=Sum('Somme_gnf')).order_by('date')

    recherche_term = request.GET.get('q')

    if recherche_term:
        # Filtrer les ventes et les dépenses en fonction du terme de recherche
        ventes_par_mois = ventes_par_mois.filter(Vehicule__icontains=recherche_term)
        depenses_par_mois = depenses_par_mois.filter(actif__icontains=recherche_term)
        
        # Si des données sont trouvées après la recherche, rediriger vers la première date trouvée
        if ventes_par_mois.exists() and depenses_par_mois.exists():
            date_trouvee = ventes_par_mois.first()['date'].month
            url = reverse('details', kwargs={'pk': date_trouvee})
            return redirect(url)

    # Calculer les totaux des ventes et dépenses pour le mois
    recapitulatif_vente = ventes_par_mois.values('date').annotate(total_vente=Sum('Somme_gnf')).order_by('date')
    recapitulatif_depense = depenses_par_mois.values('date').annotate(total_depense=Sum('Somme_gnf')).order_by('date')
    
    somme_vente = recapitulatif_vente.aggregate(total_vente_mois=Sum('total_vente'))['total_vente_mois'] or 0
    somme_depense = recapitulatif_depense.aggregate(total_depense_mois=Sum('total_depense'))['total_depense_mois'] or 0
    benefice = somme_vente - somme_depense
    vehicule=request.GET.get('q')

    context = {'vente': recapitulatif_vente, 'depenses': recapitulatif_depense,
               'mois_vente': somme_vente, 'v':vehicule,'mois_depense': somme_depense, 'benef': benefice}
    
    return render(request, 'home/details.html', context)