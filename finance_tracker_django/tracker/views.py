from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            Payment.objects.create(**form.cleaned_data)
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'tracker/add_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'tracker/payment_list.html', {'payments': payments})
