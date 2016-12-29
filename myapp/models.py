from django.db import models

class Fruits(models.Model):
    name = models.CharField('Name', max_length=30)
