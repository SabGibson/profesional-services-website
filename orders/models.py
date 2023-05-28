from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)
    paid_value = models.DecimalField(max_digits=8,decimal_places=2,blank=2,null=True)
    stripe_token =  models.CharField(max_length=255)

    class Meta:
        ordering =['-created_at']

    def __str__(self) -> str:
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2,blank=2,null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.id}'