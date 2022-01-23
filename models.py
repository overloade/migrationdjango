from django.db import models

# Create your models here.

class Pharmacist(models.Model):

    pharmacistname = models.CharField(max_length=255, default="")
    birthday = models.CharField(max_length=10, default="")
    licensenumber = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.pharmacistname

class Regions(models.Model):

    regionname = models.CharField(max_length=255, default="")
    location = models.CharField(max_length=255, default="")
    pharmaciescount = models.IntegerField(max_length=4, default=0)

    def __str__(self):
        return self.regionname


class Fines(models.Model):

    pharmacyname = models.CharField(max_length=255, default="")
    finescount = models.IntegerField(max_length=4, default=0)

    def __str__(self):
        return self.pharmacyname

