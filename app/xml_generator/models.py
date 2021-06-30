from django.db import models


class Xml(models.Model):

    information1 = models.CharField('Information 1', blank=False, max_length=255)
    information2 = models.CharField('Information 2', blank=False , max_length=255)
    information3 = models.CharField('Information 3', blank=False, max_length=255)


    def __str__(self):
        return self.information1