from django.db import models
from django.contrib.auth.models import User

class FurnitureItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    material = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='furniture_images/')

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FurnitureItem, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)  # ✅ Fixed typo here

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
