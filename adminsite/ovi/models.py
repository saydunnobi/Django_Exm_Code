from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.IntegerField()
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to="image")
    #color = models.CharField(max_length=1)
    size = models.CharField(max_length=1  )
    price = models.IntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at', )
    
    def __str__(self):
        return self.name
