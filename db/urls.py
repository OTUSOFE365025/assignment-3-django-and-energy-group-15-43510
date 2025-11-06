from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_product, name='scan_product'),
]
