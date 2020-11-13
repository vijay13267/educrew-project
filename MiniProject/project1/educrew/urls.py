from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('explore/', views.explore, name="explore"),
]
