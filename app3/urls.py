from . import views
from django.urls import path

urlpatterns = [
    path('add_card/', views.add_card, name='add_card'),
    path('my_cards/', views.my_cards, name='my_cards'),
]

