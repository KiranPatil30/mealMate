from django.http import HttpResponse
from django.shortcuts import render

from .models import Cart, CartItem, Customer, Item, Restaurant


def index(request):
    return render( request,'delivery/index.html')


def open_signin(request):
    return render(request, 'delivery/signin.html')


def open_signup(request):
    return render(request, 'delivery/signup.html')


def open_add_restaurant(request):
     return render(request, 'delivery/add_restaurant.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')

        try:
            Customer.objects.get(
            username=username)
            return HttpResponse("<h1>Duplicate USername</h1>")
        
        except:
            Customer.objects.create(
                username =username,
                password=password,
                email= email,
                mobile=mobile,
                address=address
            )

    return render(request, "delivery/signin.html")



def signin(request):
    restaurants = Restaurant.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            Customer.objects.get(username=username,password=password)

            # if customer.password == password:  # ⚠️ Only if stored as plain text (not recommended)
            if username == "admin":
                    return render(request, 'delivery/admin_home.html')
            else:
                    return render(request, 'delivery/customer_home.html',{'restaurants': restaurants,'username':username})
            # else:
            #     return HttpResponse("Login failed")

        except Customer.DoesNotExist:
            return HttpResponse("Login failed")



def add_restaurant(request):
    if request.method == 'POST':
          name = request.POST.get('name')
          picture = request.POST.get('picture')
          cuisine = request.POST.get('cuisine')
          rating = request.POST.get('rating')

          try:
               Restaurant.objects.get(name = name)
               return HttpResponse("Duplicate restaurant !")
          
          except:
               Restaurant.objects.create(
                    name = name,
                    picture =picture,
                    cuisine =cuisine,
                    rating = rating
               )
    return render(request, 'delivery/admin_home.html')
               


def open_show_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurant.html', {'restaurants': restaurants})


def open_update_restaurant(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    return render(request, 'delivery/update_restaurant.html', {"restaurant" : restaurant})

def update_restaurant_data(request, res_id):
    if request.method == 'POST':
        restaurant = Restaurant.objects.get(id=res_id)

        restaurant.name = request.POST.get('name')
        restaurant.picture = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')

        restaurant.save()
        return redirect('open_show_restaurant')



from django.shortcuts import redirect

def open_delete_restaurant(request, res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    restaurant.delete()
    return redirect('open_show_restaurant')



def open_update_menu(request, res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    # itemList = Item.objects.filter(restaurant=restaurant)
    itemList = restaurant.items.all()

    return render(request, 'delivery/update_menu.html', {"itemList": itemList, "restaurant": restaurant})

    # itemList = Item.objects.all()
    # return render(request, 'delivery/update_menu.html', {"itemList" : itemList,"restaurant": restaurant})


def update_menu(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)

    if request.method == 'POST':
          name = request.POST.get('name')
          description = request.POST.get('description')
          price = request.POST.get('price')
          vegitarian = request.POST.get('vegetarian') == 'on'
          image = request.POST.get('picture')


          try:
               Item.objects.get(name = name)
               return HttpResponse("Duplicate Item")

          
          except:
                Item.objects.create(
                    restaurant = restaurant,
                    name = name,
                    description = description,
                    price = price,
                    vegitarian = vegitarian,
                    image = image
                )
               
    return render(request, 'delivery/admin_home.html')


def open_customer_menu(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'delivery/customer_home.html', {'restaurants': restaurants})



def open_view_cutomer_menu(request,res_id,username):
    restaurant = Restaurant.objects.get(id=res_id)
    # itemList = Item.objects.filter(restaurant=restaurant)
    itemList = restaurant.items.all()

    return render(request, 'delivery/view_menu.html', {"itemList": itemList, "username": username})





def delete_item(request, res_id):
    restaurant = Item.objects.get(id=res_id)
    restaurant.delete()
    return HttpResponse("Deleted Successfull")


# def add_to_cart(request,item_id,username):
#      item = Item.objects.get(id=item_id)
#      customer = Customer.objects.get(user=username)
     
#      cart, created = Cart.objects.get_or_create(customer=customer)

#      cart.items.add(item)
#     #  return HttpResponse("Added to Cart")
#      return render(request, 'delivery/added_cart.html', {'item': item,
#     'cart': cart,
#     'customer': customer})

def add_to_cart(request, item_id, username):
    item = Item.objects.get(id=item_id)
    customer = Customer.objects.get(username=username)
    
    # Ensure the customer has a cart
    cart, created = Cart.objects.get_or_create(customer=customer)
    
    # Check if the item already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    
    if not created:  # If it already exists, increase the quantity
        cart_item.quantity += 1
        cart_item.save()
    
    return render(request, 'delivery/added_cart.html', {'cart': cart})



def show_cart(request, username):
    customer = Customer.objects.get(username=username)
    cart = Cart.objects.get(customer=customer)
    items_in_cart = cart.items.all()

    return render(request, 'delivery/show_cart.html', {
        'customer': customer,
        'cart': cart,
        'items': items_in_cart
    })




def remove_from_cart(request, item_id, username):
    customer = get_object_or_404(Customer, username=username)
    cart = get_object_or_404(Cart, customer=customer)
    cart_item = get_object_or_404(CartItem, cart=cart, item__id=item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1  # ➖ Decrease quantity
        cart_item.save()
    else:
        cart_item.delete()  # 🗑️ Remove if quantity 0

    return redirect('show_cart', username=username)

# def show_cart(request, username):
#     customer = get_object_or_404(Customer, username=username)
#     cart = Cart.objects.get(customer=customer)
#     cart_items = cart.cart_items.select_related('item')

#     return render(request, 'delivery/cart.html', {
#         'cart': cart,
#         'cart_items': cart_items,
#         'customer': customer
#     })

def show_cart(request, username):
    # Fetch the customer
    customer = Customer.objects.get(username=username)

    # Get the cart of the customer
    cart = Cart.objects.get(customer=customer)
    
    # Get all the cart items for the customer's cart
    cart_items = cart.cart_items.all()  # Assuming CartItem is a related name for cart_items
    
    # Calculate the grand total
    grand_total = cart.total_price()  # Assuming this is the method to calculate total price

    # Pass the cart items and grand total to the template
    return render(request, 'delivery/show_cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'customer': customer
    })