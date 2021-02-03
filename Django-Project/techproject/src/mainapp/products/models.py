from django.db import models

# Create your models here.


type_choices = [
    ('appetizers', 'appetizers'),
    ('entrees', 'entrees'),
    ('treats', 'treats'),
    ('drinks', 'drinks'),
]

class Product(models.Model):
    type = models.CharField(max_length=60, choices=type_choices)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2, default=0.00)
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name