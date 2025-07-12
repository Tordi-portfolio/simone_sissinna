# store/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    selected_category = request.GET.get('category')
    if selected_category:
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
        'selected_category': selected_category
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def sell(request):
    return render(request, 'sell.html')
