from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'date_joined', 'last_login')
        write_only_fields = ('password')
        read_only_fields = ('date_joined', 'last_login')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance