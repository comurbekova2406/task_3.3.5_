from django.db import models


class Products(models.Model):
    """ Products model"""
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)


def __str__(self):
    return self.name


class Profile(models.Model):
    """Profile model"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    balance = models.IntegerField()


class Customer(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models)


class Courier(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models)


class Staff(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models)


class OrderBox(models.Model):
    """Busket model"""
    product = models.ForeignKey(to=Customer, on_delete=models.SET_NULL())
    total_price = models.PositiveIntegerField(verbose_name='TOTAL PRICE')
    ordered_at = models.DateTimeField(verbose_name='ordered_at:')
