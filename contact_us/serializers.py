from rest_framework import serializers
from .models import ContactUs
class contactSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContactUs
        fields = '__all__'