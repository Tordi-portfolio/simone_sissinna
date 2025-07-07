from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author, name='author'),
    path('gallary/', views.gallary, name='gallary'),

    # Gallery Section
    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/upload/', views.upload_gallery_view, name='upload_gallery'),

    # Fans Card Section
    path('fanscard_list', views.fanscard_list, name='fanscard_list'),
    path('upload_fanscard', views.upload_fanscard, name='upload_fanscard'),
    path('fanscard_detail/<int:pk>/', views.fanscard_detail, name='fanscard_detail'),

    path('my_fanscard/', views.my_fanscard, name='my_fanscard'),
    path('admin-upload-fanscard/', views.admin_upload_fanscard, name='admin_upload_fanscard'),
]

