from rest_framework import serializers
from .models import User, Employer
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined')
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password', 'password_confirm')
        
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data    
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
    
class EmployerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Employer
        fields = ['id', 'user', 'company_name', 'contact_person_name', 'email', 'phone_number', 'address', 'created_at']
        read_only_fields = ['id']
        
    def validate_email(self, value):
        if Employer.objects.filter(email=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value