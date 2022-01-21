from django.db import models

# Create your models here.
class Deals(models.Model):
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantity of items")
    price = models.FloatField(max_length=100, blank=False, null=False, verbose_name="price of the item")
    expiry = models.DateTimeField(verbose_name="expiry time")

    def __str__(self):
        return str(self.quantity)

class Inventory(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="unique id")
    name = models.CharField(max_length=1000, blank=False, null=False, verbose_name="name of the product")
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantity of items")
    price = models.FloatField(blank=False, null=False, verbose_name="price of the item")
    currency_name = models.CharField(max_length=10, blank=False, null=False, verbose_name="currency name")
    deal_id = models.ForeignKey(Deals, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="unique id")
    name = models.CharField(max_length=1000, blank=False, null=False, verbose_name="name of customer")
    phone_no = models.IntegerField(blank=True, null=True, verbose_name="phone no")
    email = models.EmailField(blank=True, null=True, verbose_name="email")
    deal_id = models.ManyToManyField(Deals)

