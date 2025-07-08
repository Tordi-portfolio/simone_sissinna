from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author, name='author'),
    path('gallary/', views.gallary, name='gallary'),

    # PAYMENT METHOD
    path('payment/', views.payment, name='payment'),
    path('how_to_pay/', views.how_to_pay, name='how_to_pay'),

    # Gallery Section
    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/upload/', views.upload_gallery_view, name='upload_gallery'),

    # Fans Card Section
    path('fanscard_list', views.fanscard_list, name='fanscard_list'),
    path('upload_fanscard', views.upload_fanscard, name='upload_fanscard'),
    path('fanscard_detail/<int:pk>/', views.fanscard_detail, name='fanscard_detail'),

    path('my_fanscard/', views.my_fanscard, name='my_fanscard'),
    path('admin-upload-fanscard/', views.admin_upload_fanscard, name='admin_upload_fanscard'),

    path('premiun_card/', views.premiun_card, name='premiun_card'),
]

