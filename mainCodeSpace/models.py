from django.db import models

# Create your models here.

class Attempts(models.Model):
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return "Attempts"