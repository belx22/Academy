from django.db import models

# Create your models here.

class Trajet(models.Model):
    PointDepart = models.CharField(max_length=250)
    PointArriver = models.CharField(max_length=250)
    DateDepart = models.DateTimeField(auto_now_add=True)
    DureeTrajet = models.CharField(max_length=150, default='5h')
    