from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
# Create your views here.


def view_productos(request):
    productos = Producto.objects.all()

    contexto = {
        "productos" : productos
    }

    return render(request, "productos/list.html", contexto)

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-list-products')  # Redirect to a view displaying a list of products
    else:
        form = ProductoForm()
    
    context = {'form': form}
    return render(request, 'productos/modal-product.html', context)
