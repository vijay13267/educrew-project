from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('explore/faculty/', views.exploreFaculty, name="exploreFaculty"),
    path('explore/students/', views.exploreStudents, name="exploreStudents"),
    path('announce/',views.announcement, name = "announcement")
    # path('search/<int:id>/', views.search, name="search"),

]
