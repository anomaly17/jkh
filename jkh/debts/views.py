from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from .models import Debt


class DebtPayment(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'debts/payment_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.account_type = kwargs.get('type')
        try:
            account = getattr(request.user, f"{self.account_type}_account")
        except AttributeError:
            self.debt = None
        else:
            self.debt = Debt.objects.filter(type=self.account_type, account=account, is_paid=False).first()

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'TYPES': Debt.Types,
            'type': self.account_type,
            'debt': self.debt
        })

    def post(self, request, *args, **kwargs):
        if self.debt:
            self.debt.is_paid = True
            self.debt.save()
        messages.success(request, 'Оплата прошла успешно')
        return HttpResponseRedirect(reverse_lazy('home'))

