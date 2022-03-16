from products.models import Products
from clients.models import Clients
from django.db import models

class Bills(models.Model):
    client = models.ForeignKey(
                    Clients, null=True, 
                    on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    nit = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    product = models.ForeignKey(
                    Products, null=True, 
                    on_delete=models.CASCADE)
    def __str__(self):
        return self.code


class BillsProducts(models.Model):
    bill = models.ForeignKey(
                    Bills, null=True, 
                    on_delete=models.CASCADE)
    product = models.ForeignKey(
                    Products, null=True, 
                    on_delete=models.CASCADE)
    def __str__(self):
        return self.bill.code
