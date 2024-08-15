from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    stock = models.ForeignKey(Stock, related_name='equipment', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='equipment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='equipment', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    