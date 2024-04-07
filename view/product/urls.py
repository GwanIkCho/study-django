from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from product.views import ProductView, ProductViewAPI

app_name = 'product'

urlpatterns = [
    path('',ProductView.as_view(),name='product'),
    path('<int:product_id>/',ProductViewAPI.as_view(), name='product-api')
]









