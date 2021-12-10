from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contac(models.Model):
    id_c = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)    
    telefono = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    mensaje = models.CharField(max_length=200)    
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = True
        ordering = ('id_c',)
        db_table = 'contact'

    def __str__(self):
        return self.nombre