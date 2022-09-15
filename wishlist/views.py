from wishlist.models import BarangWishlist
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

data_barang_wishlist = BarangWishlist.objects.all()

# Create your views here.


def show_wishlist(request):
    return render(request, "wishlist.html", context)


context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Fitriadc'
}


def data_show_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def data_show_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def data_show_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def data_show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
