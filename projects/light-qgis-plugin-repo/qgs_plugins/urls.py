from django.urls import path
from . import views

app_name = 'qgs_plugins'

urlpatterns = [
    path('', views.plugin_list, name='plugin_list'),
    path('download/<str:plugin_name>/', views.download_plugin, name='download'),
    path('upload/', views.upload_plugin, name='upload_plugin'),
]
