from django.db import models
class voitures(models.Model):
    v=models.CharField(max_length=500,primary_key=True,default='aucun')
    def __str__(self):
        return self.v



class sell(models.Model):
    vehicules = {('Citroen Jumper', 'CITROEN JUMPER'), ('Ford', 'FORD'), ('Toyota', 'Toyota'),
                 ("Vente à l'usine", "Vente à l'usine")}
    statut = {('payé', 'payé'), ('non payé', 'non payé')}
    
    Vehicule = models.ForeignKey(voitures,on_delete=models.PROTECT,null=True)
    vente = models.IntegerField(null=True)
    prime = models.FloatField(blank=True, null=True, default=0)  # Définir la valeur par défaut à 0
    sortie = models.IntegerField(blank=True, null=True)
    vendu = models.IntegerField(null=True)
    retourner = models.IntegerField(null=True)
    credit = models.IntegerField(blank=True, null=True)
    Somme_gnf = models.IntegerField(blank=True, null=True)
    statut_credit = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True, auto_now_add=True)

    PRIME_CITROEN = 0.1
    PRIME_DEFAULT = 0.0

    def save(self, *args, **kwargs):
        # Effectuer une opération lors de l'enregistrement du modèle
        if self.Vehicule_id in ['Toyota', 'Ford', 'Citroen jumper']:
            self.prime = self.PRIME_CITROEN
        else:
            self.prime = self.PRIME_DEFAULT
        self.sortie = self.vente
        self.Somme_gnf = ((self.vendu * 5000) - (self.prime * 5000 * self.vendu)) - self.credit
        if self.credit !=0:
            self.statut_credit='non payé'
        else:
            self.statut_credit='payé'


        if self.statut_credit == 'payé':
            self.Somme_gnf += self.credit
            self.credit = 0
        
        super(sell, self).save(*args, **kwargs)




# Create your models here.
