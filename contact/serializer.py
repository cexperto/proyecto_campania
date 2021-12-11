from rest_framework import serializers
from .models import Contac
from drf_extra_fields.fields import Base64ImageField

class AllContactSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Contac
        fields= '__all__' 