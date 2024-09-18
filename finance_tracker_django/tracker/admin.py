from django.contrib import admin
from .models import Payment, Debt, Balance, Transaction

admin.site.register(Payment)
admin.site.register(Debt)
admin.site.register(Balance)
admin.site.register(Transaction)
