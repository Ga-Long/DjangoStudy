from django.db import models

# 속성 정의
class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=False, default='')
    price = models.DecimalField(max_digits=20, decimal_places=1,blank=False, default=0)

