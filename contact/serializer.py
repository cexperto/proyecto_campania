from rest_framework import serializers
from .models import Contac
from drf_extra_fields.fields import Base64ImageField

class AllContactSerializer(serializers.ModelSerializer):
    img_factura = Base64ImageField(required=False)

    class Meta:
        model = Contac
        fields= '__all__'    
    
    def to_representation(self, instance):
        return {
            "nombre": instance.nombre,            
            "telefono": instance.telefono,
            "correo": instance.correo,
            "mensaje": instance.mensaje
        }
