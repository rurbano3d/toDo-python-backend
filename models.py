from django.db import models

class Lista (models.Model):
    nome=models.CharField(max_length=200)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.nome
