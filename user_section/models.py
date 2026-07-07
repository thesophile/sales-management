from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    Title = models.CharField(max_length=100)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

    def __str__(self):
        return self.Title
    
    
    
class Enquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='enquiries')
    name = models.CharField(max_length=100)
    address = models.TextField()
    quantity = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.product.Title}"