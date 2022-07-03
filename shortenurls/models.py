from django.db import models

# Create your models here.


class URL(models.Model):
    original = models.CharField(max_length=200)
    shorten = models.CharField(max_length=200)
    created_at = models.DateTimeField('created at')
