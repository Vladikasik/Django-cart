from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    price = models.IntegerField()
    current_volume = models.IntegerField()
    min_available_volume = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name