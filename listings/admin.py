from django.contrib import admin
from .models import Listings
# Register your models here.

class AdminListings(admin.ModelAdmin):
    list_displa=('title','city')
    list_filter=('bedrooms','bathrooms','sqft')


admin.site.register(Listings,AdminListings)
