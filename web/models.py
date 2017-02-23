from django.db import models

# Create your models here.

class Software(models.Model):
    name = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100, unique=True)
    software = models.ManyToManyField(Software, blank=True)

    def __str__(self):
        return self.name

