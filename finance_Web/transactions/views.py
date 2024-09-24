from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction


@login_required
def dashboard(request):
    # 대시보드 로직
    return render(request, 'transactions/dashboard.html')

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)