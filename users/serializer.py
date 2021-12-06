from rest_framework import serializers
from .models import Users


class AllUserSerializer(serializers.ModelSerializer):    
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
        }
    
    
