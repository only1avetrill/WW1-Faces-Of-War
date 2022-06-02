from django.urls import path
from . import views

urlpatterns = [
    path('quotes/Literature/', views.QuotesLiterature, name='quotes_Literature'),
    path('quotes/Document/', views.QuotesDocument, name='quotes_Document'),
    path('quotes/Memories/', views.QuotesMemories, name='quotes_Memories'),
]