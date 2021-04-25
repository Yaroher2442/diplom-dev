from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index', views.render_test),
    path('page/home',views.home)
]
