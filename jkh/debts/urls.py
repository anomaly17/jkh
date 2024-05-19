from django.urls import path

from .views import DebtPayment


app_name = 'debts'

urlpatterns = [
    path('<str:type>/payment/', DebtPayment.as_view(), name='debt_payment'),
]
