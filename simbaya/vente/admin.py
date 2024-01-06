from django.contrib import admin
from .models import sell
from .models import voitures

# Register your models here.
admin.site.register(sell)
admin.site.register(voitures)
