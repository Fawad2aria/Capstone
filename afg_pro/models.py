from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyCustomer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class MyCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MyProduct(models.Model):
    UNIT = (
        ('Lb', 'Lb'),
        ('Kg', 'kg'),
        ('Number', 'Number'),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=100, null=True, choices = UNIT)
    price = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ManyToManyField(MyCategory)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        )

    customer = models.ForeignKey(MyCustomer, null= True, on_delete = models.SET_NULL)
    product = models.ForeignKey(MyProduct, null= True, on_delete = models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
