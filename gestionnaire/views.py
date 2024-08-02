from django.shortcuts import render, redirect
from .models import *
from .forms import RevenusForm, BudgetsForm, ObjectifsForm, DepensesForm
from django.contrib.auth.decorators import login_required

# Vue des revenus
@login_required(login_url='/')
def revenus(request):
  revenus = Revenus.objects.all()
  return render(request, 'revenus/list_revenus.html', {'revenus': revenus})
@login_required(login_url='/')
def add_revenus(request):
  if request.method == 'POST':
    form = RevenusForm(request.POST)
    if form.is_valid():
      revenu = form.save(commit=False)
      # Ajouter la valeur au champ manquant
      revenu.proprietaire = request.user.username
      print("username : ", request.user.username)
      # Enregistrer l'instance
      revenu.save()
      return redirect('revenus')
  else:
    form = RevenusForm()
  return render(request, 'revenus/add_revenus.html', {'form': form})
@login_required(login_url='/')
def update_revenus(request, pk):
  revenus = Revenus.objects.get(id=pk)
  if request.method == 'POST':
    form = RevenusForm(request.POST, instance=revenus)
    if form.is_valid():
      form.save()
      return redirect('revenus')
  else:
    form = RevenusForm(instance=revenus)
  return render(request, 'revenus/update_revenus.html', {'form': form})

@login_required(login_url='/')
def remove_revenus(request, pk):
  revenus = Revenus.objects.get(id=pk)
  if request.method == 'POST':
    revenus.delete()
    return redirect('revenus')
  return render(request, 'revenus/remove_revenus.html', {'revenus': revenus})

#vue des budgets
@login_required(login_url='/')
def budgets(request):
  budgets = Budgets.objects.all()
  return render(request, 'budgets/list_budgets.html', {'budgets': budgets})

@login_required(login_url='/')
def add_budgets(request):
  if request.method == 'POST':
    form = BudgetsForm(request.POST)
    if form.is_valid():
      budget = form.save(commit=False)
      # Ajouter la valeur au champ manquant
      budget.proprietaire = request.user.username
      # Enregistrer l'instance
      budget.save()
      return redirect('budgets')
  else:
    form = BudgetsForm()
  return render(request, 'budgets/add_budgets.html', {'form': form})

@login_required(login_url='/')
def update_budgets(request, pk):
  budgets = Budgets.objects.get(id=pk)
  if request.method == 'POST':
    form = BudgetsForm(request.POST, instance=budgets)
    if form.is_valid():
      form.save()
      return redirect('budgets')
  else:
    form = BudgetsForm(instance=budgets)
  return render(request, 'budgets/update_budgets.html', {'form': form})

@login_required(login_url='/')
def remove_budgets(request, pk):
  budgets = Budgets.objects.get(id=pk)
  if request.method == 'POST':
    budgets.delete()
    return redirect('budgets')
  return render(request, 'budgets/remove_budgets.html', {'budgets': budgets})

#vue des objectifs
@login_required(login_url='/')
def list_objectifs(request):
  objectifs = Objectifs.objects.all()
  return render(request, 'objectifs/list_objectifs.html', {'objectifs': objectifs})

@login_required(login_url='/')
def add_objectifs(request):
  if request.method == 'POST':
    form = ObjectifsForm(request.POST)
    if form.is_valid():
      objectif = form.save(commit=False)
      # Ajouter la valeur au champ manquant
      objectif.proprietaire = request.user.username
      # Enregistrer l'instance
      objectif.save()
      return redirect('objectifs')
  else:
    form = ObjectifsForm()
  return render(request, 'objectifs/add_objectifs.html', {'form': form})

@login_required(login_url='/')
def update_objectifs(request, pk):
  objectifs = Objectifs.objects.get(id=pk)
  if request.method == 'POST':
    form = ObjectifsForm(request.POST, instance=objectifs)
    if form.is_valid():
      form.save()
      return redirect('objectifs')
  else:
    form = ObjectifsForm(instance=objectifs)
  return render(request, 'objectifs/update_objectifs.html', {'form': form})

@login_required(login_url='/')
def remove_objectifs(request, pk):
  objectifs = Objectifs.objects.get(id=pk)
  if request.method == 'POST':
    objectifs.delete()
    return redirect('objectifs')
  return render(request, 'objectifs/remove_objectifs.html', {'objectifs': objectifs})

#vue des depenses
@login_required(login_url='/')
def list_depenses(request):
  depenses = Depenses.objects.all()
  return render(request, 'depenses/list_depenses.html', {'depenses': depenses})

@login_required(login_url='/')
def add_depenses(request):
  if request.method == 'POST':
    form = DepensesForm(request.POST)
    if form.is_valid():
      depense = form.save(commit=False)
      # Ajouter la valeur au champ manquant
      depense.proprietaire = request.user.username
      # Enregistrer l'instance
      depense.save()
      return redirect('depenses')
  else:
    form = DepensesForm()
  return render(request, 'depenses/add_depenses.html', {'form': form})

@login_required(login_url='/')
def update_depenses(request, pk):
  depenses = Depenses.objects.get(id=pk)
  if request.method == 'POST':
    form = DepensesForm(request.POST, instance=depenses)
    if form.is_valid():
      form.save()
      return redirect('depenses')
  else:
    form = DepensesForm(instance=depenses)
  return render(request, 'depenses/update_depenses.html', {'form': form})

@login_required(login_url='/')
def remove_depenses(request, pk):
  depenses = Depenses.objects.get(id=pk)
  if request.method == 'POST':
    depenses.delete()
    return redirect('depenses')
  return render(request, 'depenses/remove_depenses.html', {'depenses': depenses})

