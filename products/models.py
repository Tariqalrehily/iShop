from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    brand = models.CharField(max_length=200, default='')
    year = models.IntegerField(default='')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'slug')

    
