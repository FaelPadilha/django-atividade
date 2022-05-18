from django.db import models

# Create your models here.
class Banco(models.Model):
    CODIGO = models.AutoField(primary_key=True)
    NOME = models.CharField(max_length=100, null=False)
    ENDERECO = models.CharField(max_length=150, null=False)
