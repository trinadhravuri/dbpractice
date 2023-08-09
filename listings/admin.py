from django.contrib import admin
from .models import Listings
# Register your models here.

class AdminListings(admin.ModelAdmin):
    list_display=('id','title','city')
    list_display_links = ('id','title')
    list_filter=('bedrooms','bathrooms','sqft')
    search_fields = ('title','description','city','address','Zipcode','price')

admin.site.register(Listings,AdminListings)
