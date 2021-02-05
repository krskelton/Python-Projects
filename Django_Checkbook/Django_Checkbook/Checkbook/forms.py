from django.forms import ModelForm
from .models import Account, Transaction

# create account form
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

# create transaction form
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
