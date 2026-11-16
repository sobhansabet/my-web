from django.db import models
class contact(models.Model):
    text = models.CharField(max_length=32)
    email = models.EmailField()
    pim = models.TextField()
    