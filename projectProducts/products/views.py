from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.


def home(request):
    products = Product.objects.all().values()
    return render(request, 'partials/table.html', {'products': products})


def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'partials/form.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'partials/form.html', {'form': form})
