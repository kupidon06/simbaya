from django import forms
from .models import sell

class seller(forms.ModelForm):
    class Meta():
        model=sell
        fields=['Vehicule','vente','vendu','retourner','credit']
        
