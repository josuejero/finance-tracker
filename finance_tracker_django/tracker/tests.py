from django.test import TestCase
from .models import Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(description="Test Payment", amount=100.0, balance=500.0)

    def test_payment_balance(self):
        payment = Payment.objects.get(description="Test Payment")
        self.assertEqual(payment.amount, 100.0)
        self.assertEqual(payment.balance, 500.0)

    def test_update_balance(self):
        payment = Payment.objects.get(description="Test Payment")
        initial_balance = payment.balance
        payment.balance -= payment.amount
        payment.save()
        self.assertEqual(payment.balance, initial_balance - payment.amount)
