from wishlist.models import BarangWishlist
from django.shortcuts import render
from django.shortcuts import render
data_barang_wishlist = BarangWishlist.objects.all()

# Create your views here.


def show_wishlist(request):
    return render(request, "wishlist.html", context)


context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Fitriadc'
}


...
