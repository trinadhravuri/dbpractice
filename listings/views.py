from django.shortcuts import render
from .models import Listings
# Create your views here.


def listings_pro(request):
    lists = Listings.objects.all()
    context = {
        'lists':lists,
    }
    return render(request,'listings/listings.html',context)