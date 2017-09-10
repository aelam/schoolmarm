from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from collections import OrderedDict
from .models import *


UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ('url', 'username', 'email', 'groups')

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MarketChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketChannel
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super(MarketChannelSerializer, self).to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(StudentSerializer, self).to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret
