from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.index),
    path('open_signin', views.open_signin,name='open_singin'),
    path('open_signup', views.open_signup,name='open_signup'),
    path('signup',views.signup, name='signup'),
    path('singin',views.signin,name='signin'),
    path('open_add_restaurant',views.open_add_restaurant,name='open_add_restaurant'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant_data'), 
    # path('show_restaurant/', views.open_show_restaurant, name='open_show_restaurant'), 
    path('open_show_restaurant/', views.open_show_restaurant, name='open_show_restaurant'),

    path('open_update_restaurant/<int:res_id>', views.open_update_restaurant, name='open_update_restaurant'),
    path('update_restaurant_data/<int:res_id>', views.update_restaurant_data, name='update_restaurant_data'),


    path('open_delete_restaurant/<int:res_id>', views.open_delete_restaurant, name='open_delete_restaurant'),
    path('open_update_menu/<int:res_id>', views.open_update_menu, name='open_update_menu'),

    path('update_menu/<int:res_id>', views.update_menu, name='update_menu'),

    path('open_customer_menu/', views.open_customer_menu, name='open_customer_menu'),

    path('open_view_cutomer_menu/<int:res_id>/<str:username>', views.open_view_cutomer_menu, name='open_view_cutomer_menu'),

    path('delete_item/<int:res_id>', views.delete_item, name='delete_item'),
    # path('add_to_cart/<int:res_id>', views.add_to_cart, name='add_to_cart'),
    # path('cart/<str:username>/', views.show_cart, name='show_cart'),
    path('add_to_cart/<int:item_id>/<str:username>/', views.add_to_cart, name='add_to_cart'),
    path('show_cart/<str:username>', views.show_cart, name='show_cart'),
    path('checkout/<str:username>', views.checkout, name='checkout'),
    # path('checkout/<str:username>/', views.checkout, name='checkout'),

    path('orders/<str:username>/', views.orders, name='orders'),

    


    
]
