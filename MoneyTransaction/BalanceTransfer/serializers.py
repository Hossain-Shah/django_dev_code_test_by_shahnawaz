from rest_framework import serializers
from django.contrib.auth.models import User
from BalanceTransfer.models import balance


class balanceSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    class Meta:
        model = balance
        fields = ['id', 'user', 'balance']


class RegistrationLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
