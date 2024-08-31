from django.contrib import admin
from .models import BankAccount, Transaction, LoginLogoutHistory

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'account_type', 'balance')
    search_fields = ('account_number', 'user__username')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'timestamp')
    search_fields = ('account__account_number', 'transaction_type')

@admin.register(LoginLogoutHistory)
class LoginLogoutHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')
