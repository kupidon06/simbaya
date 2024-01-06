# urls.py

from django.urls import path
from .views import ventes_mois_en_cours, rap, details,recherche

urlpatterns = [
    path('', ventes_mois_en_cours, name='ventes_mois_en_cours'),
    path('rapport/', rap,name='rapport'),
    path('details/<int:pk>/', details, name='details'),
    # Vue de recherche pour filtrer les ventes
    path('ma_vues/', recherche, name='ma_vues'),
]
