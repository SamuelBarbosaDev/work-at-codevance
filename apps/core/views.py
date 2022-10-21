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
        #===============Checks if the expiration date has been reached===============
        today = datetime.date.today()
        payments_model = Payments.objects.filter(request_status='Disponível', user=self.request.user.id)

        for paymens_model in payments_model:
            if paymens_model.expiration_date < today:
                Payments.objects.filter(request_status='Disponível', user=self.request.user.id).update(request_status='Indisponível')

        return context

    def get_queryset(self):
        return Payments.objects.filter(user=self.request.user.id).order_by('-date_of_issue').exclude(request_status='Indisponível')

payments_list_view = PaymentsListView.as_view()


class HistoryListView(ListView):
    model = Payments
    template_name = 'core/pages/history.html'
    context_object_name = 'payments'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(HistoryListView, self).get_context_data(**kwargs)
        context.update({
        })
        return context

    def get_queryset(self):
        return Payments.objects.filter(user=self.request.user.id).order_by('-date_of_issue')

history_list_view = HistoryListView.as_view()