from django.db import models
from django.forms import EmailField

class Autor (models.Model):
    autor = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.autor} {self.email}"