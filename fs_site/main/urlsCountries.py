from django.urls import path
from . import views

urlpatterns = [
    path('faces-of-war/France/', views.FacesOfWarFrance, name='faces_of_war_FRANCE'),
    path('faces-of-war/Russia/', views.FacesOfWarRussia, name='faces_of_war_RUSSIA'),
    path('faces-of-war/GreatBritain/', views.FacesOfWarGreatBritain, name='faces_of_war_GREATBRITAIN'),
    path('faces-of-war/USA/', views.FacesOfWarUSA, name='faces_of_war_USA'),
    path('faces-of-war/Serbia/', views.FacesOfWarSerbia, name='faces_of_war_SERBIA'),
    path('faces-of-war/Belgium/', views.FacesOfWarBelgium, name='faces_of_war_BELGIUM'),
    path('faces-of-war/Italy/', views.FacesOfWarItaly, name='faces_of_war_ITALY'),
    path('faces-of-war/Germany/', views.FacesOfWarGermany, name='faces_of_war_GERMANY'),
    path('faces-of-war/AustriaHungary/', views.FacesOfWarAustriaHungary, name='faces_of_war_AUSTRIAHUNGARY'),
    path('faces-of-war/Ottoman/', views.FacesOfWarOttoman, name='faces_of_war_OTTOMAN'),
    path('faces-of-war/Bulgary/', views.FacesOfWarBulgary, name='faces_of_war_BULGARY'),

    path('faces-of-war/Combatants/', views.Combatants, name='faces_of_war_COMBATANTS'),
    path('faces-of-war/NonCombatants/', views.NonCombatants, name='faces_of_war_NONCOMBATANTS'),
]