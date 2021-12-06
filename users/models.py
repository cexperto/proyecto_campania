from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    id_u = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    cedula = models.IntegerField(unique=True)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=200)
    user_instagram = models.CharField(max_length=200)
    factura = models.CharField(max_length=200)
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = True
        ordering = ('id_u',)
        db_table = 'users'

    def __str__(self):
        return self.nombre