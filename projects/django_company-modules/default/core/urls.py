from django.urls import path
from django.conf import settings
from . import views


app_name = "core"

urlpatterns = [
    path("create-objects/", views.dev_fill_tables, name="create_objects"),
]
