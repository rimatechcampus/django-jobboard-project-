from django.db import models

# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.email)
