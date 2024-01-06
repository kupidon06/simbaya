from django.db import models



class spend(models.Model):
    vehicules = {('Citroen Jumper', 'CITROEN JUMPER'), ('Ford', 'FORD'), ('Toyota', 'Toyota'),
                 ("usine", "usine"),('autres',('autres'))}
    typ_d = {('charge ordinaire', 'charge ordinaire'), ('charge familliale', 'charge familliale')}
   
    
    
    
    actif = models.CharField(max_length=200, null=True, choices=vehicules)
    type_depense = models.CharField(blank=True,max_length=200, null=True, choices=typ_d)
    detail = models.TextField(max_length=1000, null=True)  
    Somme_gnf = models.IntegerField(blank=True, null=True)
    date = models.DateField(null=True, blank=True, auto_now_add=True)


    def save(self, *args, **kwargs):
        # Effectuer une opération lors de l'enregistrement du modèle

        if self.actif in ['Citroen Jumper', 'Ford', 'Toyota','usine']:
            self.type_depense = 'charge ordinaire'
        else:
            self.type_depense = 'charge familliale'
        super(spend, self).save(*args, **kwargs)
    def __str__():
        return str(self.date)




# Create your models here.
