from django.db import models

# Create your models here.

class Product(models.Model):
    Title = models.CharField(max_length=100)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.Title
