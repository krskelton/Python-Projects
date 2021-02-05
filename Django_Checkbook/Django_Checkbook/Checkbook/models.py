from django.db import models

class Account(models.Model):
    # create account model attributes
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # object manager
    Accounts = models.Manager()

    # Allows references to a specific account be returned
    # as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
    # create transaction model attributes
    date = models.DateField()
    # get drop menu from choices above
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # object manager
    Transactions = models.Manager()
