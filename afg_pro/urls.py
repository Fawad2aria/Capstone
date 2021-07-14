from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'afg_pro'
urlpatterns = [
    path('signup/', views.SignupView, name='signup'),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),

    path('', views.home, name="home"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('create_order/<str:pk>', views.Creating_order, name="create_order"),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.MyProducts, name="products"),
    path('add_new/', views.Add_New_Product, name="add_new"),
    path('delete_product/<int:pro_id>', views.delete_products, name='delete_product'),
    path('edit_product/<str:pk>/', views.edit_products, name='edit_product'),

    path('users/<str:cust_id>', views.EachCustOrders_View, name="users"),
    path('delete_page/<str:order_id>', views.delete_orders, name='delete_page'),
    path('edit_page/<str:pk>/', views.edit_orders, name='edit_page'),

       path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="afg_pro/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="afg_pro/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="afg_pro/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="afg_pro/password_reset_done.html"), 
        name="password_reset_complete"),

]