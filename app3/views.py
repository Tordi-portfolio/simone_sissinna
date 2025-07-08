from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FanCard
from .forms import FanCardForm

@login_required
def add_card(request):
    if request.method == 'POST':
        form = FanCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_cards')  # or redirect wherever you want
    else:
        form = FanCardForm()
    return render(request, 'add_card.html', {'form': form})

@login_required
def my_cards(request):
    cards = request.user.fan_cards.all()
    return render(request, 'my_cards.html', {'cards': cards})
