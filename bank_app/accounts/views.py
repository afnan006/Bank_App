from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import BankAccount, Transaction, LoginLogoutHistory
from .serializers import UserSerializer, BankAccountSerializer, TransactionSerializer, LoginLogoutHistorySerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BankAccountCreateView(generics.CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        transaction_type = serializer.validated_data['transaction_type']
        amount = serializer.validated_data['amount']
        account = serializer.validated_data['account']

        if transaction_type == 'deposit':
            account.balance += amount
        elif transaction_type == 'withdraw':
            if account.balance >= amount:
                account.balance -= amount
            else:
                raise serializers.ValidationError("Insufficient balance")

        account.save()
        serializer.save()

class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(account__user=self.request.user)

class LoginLogoutHistoryView(generics.ListAPIView):
    serializer_class = LoginLogoutHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LoginLogoutHistory.objects.filter(user=self.request.user)
