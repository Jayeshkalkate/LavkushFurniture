from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist, FurnitureItem

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(FurnitureItem, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    item.delete()
    return redirect('view_wishlist')
