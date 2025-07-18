from django.urls import include, path
from . import views


app_name = "warehouse"

urlpatterns = [
    path("select2/", include("django_select2.urls"), name="django_select2"),
    path("", views.index, name="index"),
    path("inventory/", views.index, name="inventory"),
    path("orders/", views.orders, name="orders"),
    path("orders/new/", views.new_order, name="new"),
    path("orders/list/", views.list_orders, name="list"),
    # path('new_delivery', views.new_delivery, name='new_delivery'),
]
