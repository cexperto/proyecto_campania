from rest_framework import serializers
from .models import Users
from drf_extra_fields.fields import Base64ImageField

class AllUserSerializer(serializers.ModelSerializer):
    img_factura = Base64ImageField(required=False)

    class Meta:
        model = Users
        fields= '__all__'
    
    def to_representation(self, instance):
        return {
            "nombre": instance.nombre,            
            "cedula": instance.cedula,
            "telefono": instance.telefono,
            "correo": instance.correo,
            "user_instagram": instance.user_instagram,
            "factura": instance.factura,
            "img_factura": instance.img_factura
        }
    
    
