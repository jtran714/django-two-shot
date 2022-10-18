from django import forms
from receipts.models import ExpenseCategory, Receipt, Account


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = (
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ("name",)


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            "name",
            "number",
        )
