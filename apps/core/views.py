from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from core.models import *
import datetime
from django.contrib.auth.models import User

# Create your views here.

class PaymentsListView(ListView):
    model = Payments
    template_name = 'core/pages/payments.html'
    context_object_name = 'payments'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PaymentsListView, self).get_context_data(**kwargs)
        context.update({
        })
        return context

    def get_queryset(self):
        return Payments.objects.all().order_by('-date_of_issue')

payments_list_view = PaymentsListView.as_view()


class HistoryListView(ListView):
    model = Payments
    template_name = 'core/pages/history.html'
    context_object_name = 'payments'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(HistoryListView, self).get_context_data(**kwargs)
        hoje = datetime.date.today()
        context.update({
            'hoje': hoje,
        })
        return context

    def get_queryset(self):
        return Payments.objects.all().order_by('-date_of_issue')

history_list_view = HistoryListView.as_view()