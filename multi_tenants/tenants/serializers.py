from rest_framwork import serializers
from .models import CustomUser,Tenant,Media

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tenant
        field='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        field=['id','username','email','tenant']

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Media
        field=['id','tenant','file','uploaded_at']