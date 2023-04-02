from django.db import models
from uuid import uuid4

# Create your models here.

class Movies (models.Model):
    id_filme = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=120)
    duração = models.CharField(max_length=10)
    data = models.CharField(max_length=10)
    nota = models.CharField(max_length=3)
