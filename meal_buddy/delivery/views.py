from django.http import HttpResponse
from django.shortcuts import render

from .models import Customer, Item, Restaurant


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


def add_to_cart(request,item_id,username):
     return HttpResponse("Added to Cart")

