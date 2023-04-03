from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    
    path("about/", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("blog", views.blog, name="Blog"),
    path("service", views.serve, name="Services"),
    path("sell_product", views.sell_product_view, name="sell_product"),
    path("sell", views.sell, name="Sell"),
    path("buy", views.buy, name="buy"),
    path("products_url", views.cart_products, name="products_url"),
    path("cart", views.cart, name="Cart"),
    path("crop/<int:pk>", views.single_crop, name="crop"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("jobs", views.jobs, name="jobs"),
    path("worker_form", views.worker_view, name="worker_form"),
    path("user_to_us", views.user_to_us_view, name="user_to_us"),
    path("check_status", views.check_status, name="check_status"),
]