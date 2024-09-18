from django.db import models

class Payment(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    frequency = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Debt(models.Model):
    description = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    min_payment = models.DecimalField(max_digits=10, decimal_places=2)
    apr = models.DecimalField(max_digits=5, decimal_places=2)

class Balance(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
