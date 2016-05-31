from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Product, Manufacturer


def list_products(request):
    print('list_products')
    products = Product.objects.all()
    manufacturers = Manufacturer.objects.all()
    context = {
        'products': products,
        'manufacturers': manufacturers
    }
    return render(request, 'store/list_products.html', context)


def create(request):
    print('create')
    if request.method != 'POST':
        return redirect('/products/')

    print('POST', request.POST)
    try:
        if len(request.POST['name']) >= 8 and float(request.POST['price']) >= 0 and len(request.POST['description']) > 0:
            product = Product(
                name=request.POST['name'],
                price=request.POST['price'],
                description=request.POST['description'],
                manufacturer_id=request.POST['manufacturer']
            )
            product.save()
            print('product save')
        else:
            raise ValidationError('failed')
    except ValidationError:
        print('ValidationError')
    except ValueError:
        print('ValueError')

    print('redirect')
    return redirect('/products/')


def edit(request, product_id):
    print('edit', product_id)
    try:
        product = Product.objects.get(id=product_id)
        print('product', product)
    except Product.DoesNotExist:
        print('DoesNotExist')
        return redirect('/products')

    manufacturers = Manufacturer.objects.all()
    context = {
        'product': product,
        'manufacturers': manufacturers,
    }
    return render(request, 'store/edit_product.html', context)


def update(request, product_id):
    print('update', product_id)
    if request.method != 'POST':
        return redirect('/')

    print('POST', request.POST)

    try:
        if len(request.POST['name']) >= 8 and float(request.POST['price']) >= 0 and len(request.POST['description']) > 0:
            product = Product.objects.get(id=product_id)
            product.name = request.POST['name']
            product.price = request.POST['price']
            product.description = request.POST['description']
            product.manufacturer_id = request.POST['manufacturer']
            product.save()
            print('product save')
        else:
            raise ValidationError('failed')
    except ValidationError:
        print('ValidationError')
    except ValueError:
        print('ValueError')
    except Product.DoesNotExist:
        print('DoesNotExist')

    print('redirect')
    return redirect('/products/')
