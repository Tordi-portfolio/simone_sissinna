from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Shipment
from .forms import ShipmentForm

@login_required
def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.user = request.user
            shipment.save()
            return render(request, 'tracking/shipment_success.html', {
                'tracking_id': shipment.tracking_id,
                'message': 'Shipment created successfully!'
            })
    else:
        form = ShipmentForm()
    return render(request, 'tracking/create_shipment.html', {'form': form})


def track_shipment(request):
    if request.method == 'POST':
        tracking_id = request.POST['tracking_id']
        try:
            shipment = Shipment.objects.get(tracking_id=tracking_id)
            return render(request, 'tracking/tracking_result.html', {'shipment': shipment})
        except Shipment.DoesNotExist:
            return render(request, 'tracking/tracking_result.html', {'error': 'Tracking ID not found'})
    return render(request, 'tracking/track_shipment.html')