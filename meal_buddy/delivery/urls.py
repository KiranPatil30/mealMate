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


    
]
