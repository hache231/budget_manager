from django.shortcuts import render, redirect
from .models import *
from .forms import RevenusForm, BudgetsForm, ObjectifsForm, DepensesForm


# Vue des revenus
def revenus(request):
  revenus = Revenus.objects.all()
  return render(request, 'revenus/list_revenus.html', {'revenus': revenus})

def add_revenus(request):
  if request.method == 'POST':
    form = RevenusForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('revenus')
  else:
    form = RevenusForm()
  return render(request, 'revenus/add_revenus.html', {'form': form})

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

def remove_revenus(request, pk):
  revenus = Revenus.objects.get(id=pk)
  if request.method == 'POST':
    revenus.delete()
    return redirect('revenus')
  return render(request, 'revenus/remove_revenus.html', {'revenus': revenus})

#vue des budgets
def budgets(request):
  budgets = Budgets.objects.all()
  return render(request, 'budgets/list_budgets.html', {'budgets': budgets})

def add_budgets(request):
  if request.method == 'POST':
    form = BudgetsForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('budgets')
  else:
    form = BudgetsForm()
  return render(request, 'budgets/add_budgets.html', {'form': form})

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

def remove_budgets(request, pk):
  budgets = Budgets.objects.get(id=pk)
  if request.method == 'POST':
    budgets.delete()
    return redirect('budgets')
  return render(request, 'budgets/remove_budgets.html', {'budgets': budgets})

#vue des objectifs
def list_objectifs(request):
  objectifs = Objectifs.objects.all()
  return render(request, 'objectifs/list_objectifs.html', {'objectifs': objectifs})

def add_objectifs(request):
  if request.method == 'POST':
    form = ObjectifsForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('objectifs')
  else:
    form = ObjectifsForm()
  return render(request, 'objectifs/add_objectifs.html', {'form': form})

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

def remove_objectifs(request, pk):
  objectifs = Objectifs.objects.get(id=pk)
  if request.method == 'POST':
    objectifs.delete()
    return redirect('objectifs')
  return render(request, 'objectifs/remove_objectifs.html', {'objectifs': objectifs})

#vue des depenses
def list_depenses(request):
  depenses = Depenses.objects.all()
  return render(request, 'depenses/list_depenses.html', {'depenses': depenses})

def add_depenses(request):
  if request.method == 'POST':
    form = DepensesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('depenses')
  else:
    form = DepensesForm()
  return render(request, 'depenses/add_depenses.html', {'form': form})

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

def remove_depenses(request, pk):
  depenses = Depenses.objects.get(id=pk)
  if request.method == 'POST':
    depenses.delete()
    return redirect('depenses')
  return render(request, 'depenses/remove_depenses.html', {'depenses': depenses})

