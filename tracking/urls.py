from . import views
from django.urls import path

urlpatterns = [
    path('create_shipment', views.create_shipment, name='create_shipment'),
    path('track_shipment', views.track_shipment, name='track_shipment'),
    path('donate/', views.donate, name='donate'),
    path('doante_payment/', views.doante_payment, name='doante_payment'),
]

