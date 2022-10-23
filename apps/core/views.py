from django.views.generic import ListView, RedirectView
from django.urls import reverse
import datetime
import logging

from core.models import (
    Request,
    Payments,
    Supplier,
)


logger = logging.getLogger('django')


class RequestStatusRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, id):
        if id:
            try:
                payment_model = Payments.objects.filter(id=id)[0]
                request_model = Request.objects.filter(payments=payment_model)[0]

            except IndexError:
                request_create = Request.objects.create(
                    payments=payment_model,
                    requests='Solicitado',
                )
                payment_status = Payments.objects.filter(id=id).update(request_status='Aguardando confirmação')
                logger.warning("Request made, and status changed from available to Waiting for confirmation")

        return reverse("home", kwargs={})


request_status_redirect_view = RequestStatusRedirectView.as_view()


class RequestApprovedRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, id, sp):
        request_model = Request.objects.filter(id=id).update(requests=sp)
        if sp == 'Aprovado':
            logger.warning(f"Request to change the status of models request, id:{id}, request:{sp}, has been approved.")

        elif sp == 'Negado':
            logger.warning(f"Request to change the status of models request, id:{id}, request:{sp}, was Denied.")

        else:
            logger.warning("Unexpected situation.")

        return reverse("home", kwargs={})


request_approved_redirect_view = RequestApprovedRedirectView.as_view()


class RequestsListView(ListView):
    model = Request
    template_name = 'core/pages/requests.html'
    context_object_name = 'requests'
    paginate_by = 2

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user.id).order_by('-date_of_issue')


requests_list_view = RequestsListView.as_view()


class PaymentsListView(ListView):
    model = Payments
    template_name = 'core/pages/payments.html'
    context_object_name = 'payments'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PaymentsListView, self).get_context_data(**kwargs)

        # ===============Checks if the expiration date has been reached===============
        today = datetime.date.today()
        payments_model = Payments.objects.filter(request_status='Disponível', user=self.request.user.id)

        for paymens_model_available in payments_model:
            if paymens_model_available.expiration_date < today:
                Payments.objects.filter(request_status='Disponível', user=self.request.user.id).update(
                    request_status='Indisponível')

                logger.warning("Status changed from 'Available' to 'Unavailable'.")

        # ===============Checks if the expiration date has been reached===============
        paymens_waiting_confirmation = Payments.objects.filter(
            request_status='Aguardando confirmação', user=self.request.user.id)

        for payments_model_waiting_confirmation in paymens_waiting_confirmation:
            if payments_model_waiting_confirmation.expiration_date < today:
                payment = Payments.objects.filter(request_status='Aguardando confirmação', user=self.request.user.id)

                try:
                    requests = Request.objects.filter(payments=payment)
                    for request in requests:
                        request.delete()
                        payment.update(request_status='Indisponível')

                    logger.warning("Status changed from 'Awaiting confirmation' to 'Unavailable'.")
                    logger.warning("Deleting Anticipation Request")

                except ValueError:
                    payment.update(request_status='Indisponível')

                    logger.warning("Status changed from 'Awaiting confirmation' to 'Unavailable'.")
                    logger.warning("Deleting Anticipation Request")

        # ===============Checks if the expiration date has been reached===============
        for payments_model_waiting_confirmation in paymens_waiting_confirmation:
            request_model = Request.objects.filter(payments=payments_model_waiting_confirmation)
            print(request_model)
        return context

    def get_queryset(self):
        return Payments.objects.filter(user=self.request.user.id).order_by('-date_of_issue').exclude(request_status='Indisponível')


payments_list_view = PaymentsListView.as_view()


class HistoryListView(ListView):
    model = Payments
    template_name = 'core/pages/history.html'
    context_object_name = 'payments'
    paginate_by = 2

    def get_queryset(self):
        return Payments.objects.filter(user=self.request.user.id).order_by('-date_of_issue')


history_list_view = HistoryListView.as_view()
