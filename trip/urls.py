from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_fun, name='fun1'),
]