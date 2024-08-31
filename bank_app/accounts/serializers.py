from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BankAccount, Transaction, LoginLogoutHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['user', 'account_number', 'account_type', 'balance']
        extra_kwargs = {
            'account_number': {'required': False},
            'account_type': {'default': 'savings'}
        }
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'transaction_type', 'timestamp']

class LoginLogoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginLogoutHistory
        fields = ['id', 'user', 'action', 'timestamp']
