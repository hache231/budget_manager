from django import forms
from .models import *

class RevenusForm(forms.ModelForm):
    class Meta:
        model = Revenus
        fields = ['libelle', 'montant', 'periodicite']

class ObjectifsForm(forms.ModelForm):
    class Meta:
        model = Objectifs
        fields = ['libelle', 'montant']

class BudgetsForm(forms.ModelForm):
    class Meta:
        model = Budgets
        fields = ['budget', 'description', 'date_debut', 'date_fin']

class DepensesForm(forms.ModelForm):
    class Meta:
        model = Depenses
        fields = ['montant', 'budget']


