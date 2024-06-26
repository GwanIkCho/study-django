from django.db import models
from django.db.models import F
from django.db.models.functions import Floor


class ProductManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(product_sell_price=Floor(F('product_price') * (1 - F('product_discount') / 100) / 10) * 10).filter(status=True)
