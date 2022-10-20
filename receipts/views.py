from django.shortcuts import render
from .models import Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


# @login_required
# def receipts_list(request):
#     receipts = Receipt.objects.filter(purchaser=request.user)
#     context = {
#         "receipts": receipts,
#     }
#     return render(request, "receipts/list.html", context)
