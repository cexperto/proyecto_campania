from rest_framework import serializers
from .models import Users
from drf_extra_fields.fields import Base64ImageField

class AllUserSerializer(serializers.ModelSerializer):
    img_factura = Base64ImageField(required=False)

    class Meta:
        model = Users
        fields= '__all__'
    
    
    
