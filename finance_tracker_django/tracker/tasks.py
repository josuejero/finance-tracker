from celery import shared_task
from .models import Payment

@shared_task
def update_balances():
    payments = Payment.objects.all()
    for payment in payments:
        payment.balance -= payment.amount
        payment.save()
