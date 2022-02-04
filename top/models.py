from django.db import models

# Create your models here.


class usa(models.Model):
    number = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.number
