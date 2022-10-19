from django.shortcuts import render
from .models import Receipt

# Create your views here.


def receipt_list(request):
    receipts = Receipt.object.all()
    context = {
        "show_receipt": receipts,
    }
    return render(request, "receipts/list.html", context)


