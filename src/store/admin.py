from django.contrib import admin


from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)


# Admin Site Config
admin.sites.AdminSite.site_header = 'E-commerce app'
admin.sites.AdminSite.site_title = 'E-commerce admin '
admin.sites.AdminSite.index_title = 'E-commerce'
