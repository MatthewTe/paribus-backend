from django.db import models
import uuid

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_name = models.CharField(max_length=50)
    account_value = models.FloatField(default=0)

    def __str__(self):
        return f"{self.account_name}"

    class Meta:
        verbose_name_plural = "Accounts"

class AccountTransactions(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    transaction_value = models.FloatField()
    transaction_description = models.CharField(max_length=100, blank=True, null=True)
    current_account_value = models.FloatField()

    def __str__(self):
        return f"{self.transaction_id} for account {self.account}"

    # TODO: Modify a save method to update the Account value based on the transaction value when a transaction is created.
    def save(self, *args, **kwargs):
        super(AccountTransactions, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Account Transactions"