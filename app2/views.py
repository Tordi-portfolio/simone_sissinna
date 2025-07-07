from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import GalleryImage, FansCard
from .forms import GalleryImageForm, FansCardForm

# ================= Author Page ===================
def author(request):
    return render(request, 'author.html')

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
            return redirect('fanscard_list')
    else:
        form = FansCardForm()
    return render(request, 'fanscard/upload_fanscard.html', {'form': form})

def fanscard_detail(request, pk):
    card = get_object_or_404(FansCard, pk=pk)
    return render(request, 'fanscard/fanscard_detail.html', {'card': card})
