from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def add_transaction(request):
    all_account_list = Account.objects.all()
    
    if request.method == 'POST':

        form = AddTransaction(request.POST)
        if form.is_valid():
            account = Account.objects.get(id=form.cleaned_data['accountID'])
            print(account)
            transaction = Transaction(
                timestamp = form.cleaned_data['timestamp'],
                account = account.name,
                type = form.cleaned_data['type'],
                amount = form.cleaned_data['amount'],
                remark = form.cleaned_data['remark']
            )
            if form.cleaned_data['type'] == 'Debit':
                account.balance -= form.cleaned_data['amount']
            elif form.cleaned_data['type'] == 'Credit':
                account.balance += form.cleaned_data['amount']
            account.save()
            transaction.save()
            messages.success(request, "Successfully added a new transaction!")
            return redirect('finance_management:transaction')
        else:
            messages.warning(request, "Couldn't add new transaction")
            return redirect('finance_management:transaction')

    else:
        form = AddTransaction()
        return render(request, 'transaction/add_transaction.html', {'form': form, 'account_list': all_account_list})

@user_passes_test(lambda u: u.is_superuser)
def add_account(request):
    if request.method == 'POST':

        form = AddAccount(request.POST)
        if form.is_valid():
            account = Account(
                name = form.cleaned_data['name'],
                balance = form.cleaned_data['balance'],
                currency = form.cleaned_data['currency'],
            )
            account.save()
            messages.success(request, "Successfully added a new account!")
            return redirect('finance_management:account')
        else:
            messages.warning(request, "Couldn't add new account")
            return redirect('finance_management:account')

    else:
        form = AddAccount()
        return render(request, 'account/add_account.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def account(request):
    all_account_list = Account.objects.all()

    if all_account_list is None:
        messages.error(request, "No account exists in the system.")
        return render(request, 'account/account.html', {'account_list': None})
    else:
        return render(request, 'account/account.html', {'account_list': all_account_list})

@user_passes_test(lambda u: u.is_superuser)
def transaction(request):
    all_transaction_list = Transaction.objects.all()

    if all_transaction_list is None:
        messages.error(request, "No transaction exists in the system.")
        return render(request, 'transaction/transaction.html', {'transaction_list': None})
    else:
        return render(request, 'transaction/transaction.html', {'transaction_list': all_transaction_list})

@user_passes_test(lambda u: u.is_superuser)
def account_details(request, account_id):
    account = Account.objects.get(id=account_id)
    all_transaction_list = Transaction.objects.all()
    account_transaction = []
    for transaction in all_transaction_list:
        if transaction.account == account.name:
            account_transaction.append(transaction)
    return render(request, 'account/account_details.html', {'account': account, 'account_transaction': account_transaction})
