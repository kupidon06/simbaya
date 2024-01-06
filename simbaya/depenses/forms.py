from django.forms import ModelForm
from .models import spend

class spender(ModelForm):
    class Meta():
        model=spend
        fields=['actif','detail','Somme_gnf']