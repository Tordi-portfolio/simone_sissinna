from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import GalleryImage, FansCard
from .forms import GalleryImageForm, FansCardForm
from django.contrib import messages

# ================= Author Page ===================
def author(request):
    return render(request, 'author.html')

def premiun_card(request):
    return render(request, 'fanscard/premiun_card.html')

# =============== Simple Payment Page =============
def payment(request):
    return render(request, 'payment/payment.html')

def how_to_pay(request):
    return render(request, 'payment/how_to_pay.html')


# =============== Simple Gallary Page =============
def gallary(request):
    return render(request, 'gallary.html')  # If different from gallery_view

# ================ Gallery Section ================
def gallery_view(request):
    images = GalleryImage.objects.order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})

@login_required
@user_passes_test(lambda u: u.is_staff)
def upload_gallery_view(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully uploaded a gallery...')
            return redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'upload_gallery.html', {'form': form})

# ================ Fans Card Section ==============
def fanscard_list(request):
    cards = FansCard.objects.order_by('-uploaded_at')
    return render(request, 'fanscard/fanscard_list.html', {'cards': cards})

@login_required
@user_passes_test(lambda u: u.is_staff)
def upload_fanscard(request):
    if request.method == 'POST':
        form = FansCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fanscard uploaded successfully...')
            return redirect('fanscard_list')
    else:
        form = FansCardForm()
    return render(request, 'fanscard/upload_fanscard.html', {'form': form})

def fanscard_detail(request, pk):
    card = get_object_or_404(FansCard, pk=pk)
    return render(request, 'fanscard/fanscard_detail.html', {'card': card})


# USERS FANCARD
from django.shortcuts import render, redirect
from .models import UserFanCardRecord, StoreFanCard
from .forms import AdminUploadFanCardForm
from django.contrib.auth.decorators import login_required, user_passes_test

# User View - Only see their cards
@login_required
def my_fanscard(request):
    cards = UserFanCardRecord.objects.filter(user=request.user)
    return render(request, 'my_fanscard.html', {'cards': cards})


# Admin Upload View
@user_passes_test(lambda u: u.is_staff)
def admin_upload_fanscard(request):
    if request.method == 'POST':
        form = AdminUploadFanCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully uploaded  users fan card...')
            return redirect('admin_upload_fanscard')
    else:
        form = AdminUploadFanCardForm()
    return render(request, 'admin_upload_fanscard.html', {'form': form})

