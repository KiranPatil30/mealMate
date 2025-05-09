from django.contrib import admin
from .models import Customer, Restaurant,Item,Cart,CartItem
# Register your models here.
admin.site.register(Customer)
# admin.site.register(Restaurant)
# admin.site.register(Item)
# admin.site.register(Cart)


# Registering Cart and CartItem models
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Item)
admin.site.register(Restaurant)