from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title