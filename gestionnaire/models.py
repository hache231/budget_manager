from django.db import models

# Create your models here.

class Revenus(models.Model):
  libelle = models.CharField(max_length=100)
  montant = models.FloatField()
  periodicite = models.CharField(max_length=100)
  proprietaire = models.CharField(max_length=100)
  date_creation = models.DateField(auto_now_add=True)
  date_modification = models.DateField(auto_now=True)

  def __str__(self):
    return self.libelle

class Budgets(models.Model):
  budget = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  date_debut = models.DateField()
  date_fin = models.DateField()
  proprietaire = models.CharField(max_length=100)
  date_creation = models.DateTimeField(auto_now_add=True)
  date_modification = models.DateTimeField(auto_now=True)
  # ici il faut que j'ajoute une propriete pour la periodicité

  def __str__(self):
    return self.budget

class Depenses(models.Model):
  montant = models.FloatField()
  budget = models.ForeignKey(Budgets, on_delete=models.CASCADE)
  proprietaire = models.CharField(max_length=100)
  date_creation = models.DateTimeField(auto_now_add=True)
  date_modification = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.montant)
  
class Objectifs(models.Model):
  libelle = models.CharField(max_length=100)
  montant = models.FloatField()
  proprietaire = models.CharField(max_length=100)
  date_creation = models.DateTimeField(auto_now_add=True)
  date_modification = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.libelle
