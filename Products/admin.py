from django.contrib import admin

# Register your models here.

from Products.models import Product , BookMarks , Charity

admin.site.register(Product)
admin.site.register(BookMarks)
admin.site.register(Charity)
