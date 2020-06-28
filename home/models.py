from django.db import models

# Create your models here.
class client (models.Model):
    customer_name = models.CharField(max_length = 100)
    customer_mail=models.EmailField(max_length=254)
    message = models.TextField()
