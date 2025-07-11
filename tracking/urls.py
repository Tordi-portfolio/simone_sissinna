from . import views
from django.urls import path

urlpatterns = [
    path('create_shipment', views.create_shipment, name='create_shipment'),
    path('track_shipment', views.track_shipment, name='track_shipment'),
]

