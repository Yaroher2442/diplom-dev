from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login', LoginFormView.as_view()),
    path('register', RegisterFormView.as_view()),
    path('logout', LogoutView.as_view()),
    path('', Index.as_view()),
    path('page/home', HomePage.as_view()),
    path('DragDrop', DragAndDrop.as_view()),
    path('workplace', Workplace.as_view()),

]
