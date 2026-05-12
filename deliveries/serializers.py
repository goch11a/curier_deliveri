from rest_framework import serializers
from .models import CustomeUser, Parcel, DelveryProof


class CustomeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['id', 'username', 'password', 'email', 'role', 'is_staff', "is_super"]
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None) 
        instance =self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instence, validated_data):
        instence.email = validated_data.get('email', instence.email)
        instence.username = validated_data.get('username', instence.username)
        instence.role = validated_data.get('role', instence.role)
        instence.is_super = validated_data.get('is_super', instence.is_super)
        instence.is_staff = validated_data.get('is_staff', instence.is_staff)
        if "password" in validated_data:
            instence.set_password(validated_data.pop("password"))
        instence.save()    
        return instence    





class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class DelveryProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelveryProof
        fields = '__all__'
