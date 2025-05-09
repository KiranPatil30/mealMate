from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50)


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=300)
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()


# class Item(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.CharField(max_length=400)
#     price = models.FloatField()
#     vegitarian = models.BooleanField(default= True)
#     image = models.URLField(max_length=200,default='https://i.tribune.com.pk/media/images/1590373-biryani-1513939158/1590373-biryani-1513939158.gif')
#     restaurant = models.ForeignKey(Restaurant,on_delete= models.CASCADE,related_name='items')


# class Cart(models.Model):
#     customer = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name='cart')
#     items = models.ManyToManyField("Item",related_name="carts")

#     def total_price(self):
#         return sum(item.price for item in self.items.all())
    
# class CartItem(models.Model):
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')
#     item = models.ForeignKey('Item', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def total_price(self):
#         return self.quantity * self.item.price

    
    
class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    vegitarian = models.BooleanField(default=True)
    image = models.URLField(max_length=200, default='https://i.tribune.com.pk/media/images/1590373-biryani-1513939158/1590373-biryani-1513939158.gif')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='items')


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart')

    def total_price(self):
        # Summing up the total price from all CartItems
        return sum(cart_item.total_price() for cart_item in self.cart_items.all())

    
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.item.price
