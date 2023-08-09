from django.shortcuts import render
from .models import Listings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def listings_pro(request):
    lists = Listings.objects.order_by('-list_date')
    paginator = Paginator(lists,1)
    page = request.GET.get('page')
    contents = paginator.get_page(page)
    context = {
        'lists':contents
    }
    return render(request,'listings/listings.html',context)