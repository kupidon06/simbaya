
from django.shortcuts import render,redirect
from .forms import personnels
from .models import pers
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def personnel(request):
    form=personnels()
    
    if request.method=='POST':
        form=personnels(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_personnel')
    
   
    
    context={'form':form,}

    return render (request,'personnel/personnel.html',context)
def fichier(request, pk):
    perso = pers.objects.get(id=pk)
  
    data = pers.objects.filter(id=pk)
    nom=data.first().Nom
    prenom=data.first().Prenom
    num=data.first().Telephone
    poste=data.first().poste
    salaire=data.first().salaire
    


    #-------------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------------------
   

   
    context = {'nom':nom,'prenom':prenom,'num':num,'poste':poste,'salaire':salaire}
    return render(request, 'personnel/print.html', context)

def list_personnel(request):
    data=pers.objects.all()
    context={'datap':data}

    return render (request,'personnel/list.html',context)
def update(request,pk):
    perso = pers.objects.get(id=pk)
    form=personnels(instance=perso)
    if request.method=='POST':
        form=personnels(request.POST,instance=perso)
        if form.is_valid:
            form.save(request)
            return redirect('liste_personnel')
    context={'form':form}
    
   
    return render(request,'personnel/personnel.html',context)
def remove(request,pk) :
    data=pers.objects.get(id=pk)
    data.delete()
    return redirect('liste_personnel')

def recherche(request):
    # Récupérer tous les éléments sans filtre initial
    donnée = pers.objects.all()

    # Code de recherche ici si un terme de recherche est fourni
    reshearch= request.GET.get('q')
    if reshearch:
        # Filtrer les éléments en fonction du terme de recherche
        donnée = donnée.filter(Nom__icontains=reshearch)

    context = {'datap': donnée}
    return render(request, 'personnel/list.html', context)
# views.py
def generer_fichier_excel(request, pk):
    # Convertir les paramètres de l'URL en entiers
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')

    # Extrait de l'année et du mois
  

    # Obtenez le dernier jour du mois
    

    # Créez une plage de dates pour le mois donné
    

    # Filtrer les employés en fonction de la plage de dates
    data = pers.objects.filter(id=pk)
  


    # Création d'un classeur Excel et d'une feuille
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Paiement de salaire')

    style_bold = xlwt.easyxf('font: bold on')
    style_center = xlwt.easyxf('align: horiz center')

    # Ajout d'une entête
    sheet.write_merge(2, 2, 2, 4, 'FICHE DE PAIEMENT DE SALAIRE', style_bold)
    sheet.write_merge(4, 4, 2, 4, 'Nom et Prenom:', style_bold)
    sheet.write_merge(5, 5, 2, 4, 'Poste:', style_bold)
    sheet.write_merge(6, 6, 2, 4, 'Salaire de base:', style_bold)
    sheet.write_merge(7, 7, 2, 4, 'Avance sur salaire:', style_bold)
    sheet.write_merge(22, 22, 2, 4, 'Salaire NET:', style_bold)
    sheet.write_merge(24, 24, 2, 4, 'M,', style_bold)

    # Ajout des données
    for i, i in enumerate(data, start=1):
        sheet.write(4, 6, f"{i.Nom} {i.Prenom}")
        sheet.write(5, 6, i.poste)
        sheet.write(6, 6, str(i.salaire))
        sheet.write(7, 6, 'non')
        sheet.write(22, 6, str(i.salaire))
        sheet.write(24, 6, i.Nom)
        sheet.write(24, 12, 'DR KAKE')

    # Réponse HTTP avec le contenu Excel
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename=salary_{date}.xls'
    workbook.save(response)

    return response