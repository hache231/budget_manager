from django.urls import path
from . import views

urlpatterns = [
  #urls des revenus
  path("revenus/", views.revenus, name="revenus"),
  path("add_revenus/", views.add_revenus, name="add_revenus"),
  path("update_revenus/<int:pk>/", views.update_revenus, name="update_revenus"),
  path("remove_revenus/<int:pk>/", views.remove_revenus, name="remove_revenus"),
  #urls des budgets
  path("budgets/", views.budgets, name="budgets"),
  path("add_budgets/", views.add_budgets, name="add_budgets"),
  path("update_budgets/<int:pk>/", views.update_budgets, name="update_budgets"),
  path("remove_budgets/<int:pk>/", views.remove_budgets, name="remove_budgets"),
  #urls des objectifs
  path("objectifs/", views.list_objectifs, name="objectifs"),
  path("add_objectifs/", views.add_objectifs, name="add_objectifs"),
  path("update_objectifs/<int:pk>/", views.update_objectifs, name="update_objectifs"),
  path("remove_objectifs/<int:pk>/", views.remove_objectifs, name="remove_objectifs"),
  #urls des depenses
  path("depenses/", views.list_depenses, name="depenses"),
  path("add_depenses/", views.add_depenses, name="add_depenses"),
  path("update_depenses/<int:pk>/", views.update_depenses, name="update_depenses"), 
  path("remove_depenses/<int:pk>/", views.remove_depenses, name="remove_depenses"),
]
