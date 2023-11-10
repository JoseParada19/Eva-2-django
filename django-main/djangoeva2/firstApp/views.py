from django.shortcuts import render, redirect
from .models import Cliente
from .forms import FormCliente

def lista_cliente(request):
    clientes = Cliente.objects.all()
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    return render(request, 'firstapp/lista_clientes.html', {'clientes': clientes, 'form': form})    

def registrar_cliente(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = FormCliente()

    return render(request, 'firstapp/registrar_cliente.html', {'form': form})


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = FormCliente(instance=cliente)

    return render(request, 'firstapp/editar_cliente.html', {'cliente': cliente, 'form': form})


def eliminar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return redirect('clientes')
    except Cliente.DoesNotExist:
        pass


def vista_principal(request):
    return render(request, 'contenedor.html')    