from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/menu/", views.menu, name="menu"),
    path("orders/menu/order/sub/", views.subs, name="subs"),
    path("orders/menu/order/salad/", views.salad, name="salad"),
    path("orders/menu/order/pasta/", views.pasta, name="pasta"),
    path("orders/menu/order/dinnerplatter/", views.dinnerplatter, name="dinnerplatter"),
    path("orders/menu/order/extra/", views.extra, name="order_extra"),
]
