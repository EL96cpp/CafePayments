from django.db import models

class ProductType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.ForeignKey('ProductType', on_delete=models.PROTECT, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.title