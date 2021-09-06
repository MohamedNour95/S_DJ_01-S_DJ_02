from django.db import models

# Create your models here.
class Product(models.Model):
    x =[
        ('Electronics','Electronics'),('Sports','Sports'),('Home','Home'),('Food','Food'),('Books','Books')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    photo = models.ImageField(upload_to= 'photos/%y/%m/%d')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name