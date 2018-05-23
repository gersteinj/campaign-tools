from django.db import models

# Create your models here.

class Roster(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}: {self.owner}"

class Unit(models.Model):
    unit = models.CharField(max_length=100)
    qty = models.IntegerField()
    used_in = models.ForeignKey(Roster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.unit} ({self.qty})"