from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Product, Manufacturer, Order, Cart


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


def add_cart(request):
    print('add_cart', request.POST)
    if request.method != 'POST':
        return redirect('/products/')

    try:
        order_id = request.session['order_id']
        order = Order.objects.get(id=order_id)
        print('use order')
    except (Order.DoesNotExist, KeyError) as E:
        print('make new order', E)
        order = Order(
            shipping_status = False
        )
        order.save()
        order_id = order.id
        request.session['order_id'] = order_id

    try:
        product = Product.objects.get(id=request.POST['product_id'])
        cart = Cart(
            product=product,
            order=order,
            amount=request.POST['amount'],
            unit_price=product.price
        )
        cart.save()
        print('created cart', cart)
    except Exception as E:
        print('failed creating cart', E)

    carts = len(Cart.objects.filter(order_id=order_id))
    print('catrs:',carts)

    request.session['carts'] = carts
    return redirect('/products/')


def checkout(request):
    print('checkout', request)
    context = {}
    try:
        order = Order.objects.get(id=request.session['order_id'])
        print('order:', order.id)
        carts = Cart.objects.filter(order_id=order.id)
        print('carts', carts)
        for c in carts:
            print('---', c.unit_price, c.amount, c.unit_price * c.amount)
        total = sum([float(c.unit_price) * c.amount for c in carts])
        print('total price', total)
        context.update({
            'order': order,
            'carts': carts,
            'total': total,
        })
    except Exception as E:
        print('error fetching', E)
        return redirect('/products/')

    return render(request, 'store/order.html', context)


def delete_cart(request, cart_id):
    print('delete_cart', cart_id)
    try:
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        carts = len(Cart.objects.filter(order_id=request.session['order_id']))
        request.session['carts'] = carts
    except Exception as E:
        print('deletion error', E)
        return redirect('/')

    print('deletion OK')
    return redirect('/products/checkout')


def commit_order(request):
    print('commit_order')
    if request.method != 'POST':
        return redirect('/products/checkout')

    context = {}
    try:
        if len(request.POST['name']) < 8 or len(request.POST['address']) < 8 or len(request.POST['card_number']) != 16:
            raise ValidationError('malformed shipping data')
        order = Order.objects.get(id=request.session['order_id'])
        print('order', order.id)
        order.shipping_name = request.POST['name']
        order.shipping_address = request.POST['address']
        order.card_number = request.POST['card_number']
        order.shipping_status = True
        order.save()
        del(request.session['order_id'])
        del(request.session['carts'])
        context.update({
            'order': order,
        })
        print('commit order', order.id)
    except Exception as E:
        print('commit order error', E)
        return redirect('/products/checkout')

    return render(request, 'store/finished_order.html', context)

