from django.db import models

class Product(models.Model):
    product_name = models.TextField()
    product_price = models.TextField()
    product_stock = models.TextField()

    class Meta:
        db_table = 'tbl_product'

