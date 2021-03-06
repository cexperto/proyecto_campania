from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    id_u = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(unique=True, max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    user_instagram = models.CharField(max_length=200)
    factura = models.CharField(max_length=200)
    img_factura = models.ImageField(upload_to='images')
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = True
        ordering = ('id_u',)
        db_table = 'users'

    def __str__(self):
        return self.nombre
