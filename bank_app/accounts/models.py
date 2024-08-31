from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True, blank=True)  # Changed max_length to 10
    account_type = models.CharField(max_length=20, default='savings')  # Added default value
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.get_next_account_number()
        super().save(*args, **kwargs)

    def get_next_account_number(self):
        last_account = BankAccount.objects.order_by('-id').first()
        if last_account:
            last_number = int(last_account.account_number)
            next_number = last_number + 1
        else:
            next_number = 1
        return str(next_number).zfill(10)  # Zero-pad to 10 digits

    def __str__(self):
        return f"{self.account_number} ({self.account_type})"

# Optional: Use Django signals to handle the creation of account numbers
@receiver(pre_save, sender=BankAccount)
def ensure_account_number(sender, instance, **kwargs):
    if instance._state.adding and not instance.account_number:
        instance.account_number = instance.get_next_account_number()

class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)  # 'deposit' or 'withdraw'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} on {self.timestamp}"

class LoginLogoutHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)  # 'login' or 'logout'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action} at {self.timestamp}"
