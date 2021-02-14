
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'created_at', 'updated_at', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return super(UserSerializer, self).create(attrs)

