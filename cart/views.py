from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified project to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified
    project to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """
    Remove a project from the cart.
    """
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect('view_cart')
