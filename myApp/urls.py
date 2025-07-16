from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage),
    path('shop/', views.shop),
    path("base/", views.base),
    path("login/",views.login),
    path("register/", views.register),

]
