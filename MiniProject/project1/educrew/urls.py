from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .views import ProfileView,ProfileUpdateView

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('explore/faculty/', views.exploreFaculty, name="exploreFaculty"),
    path('explore/students/', views.exploreStudents, name="exploreStudents"),
    path('view/faculty/<int:pk>', views.viewFaculty, name="viewFaculty"),
    path('view/student/<int:pk>', views.viewStudent, name="viewStudent"),
    path('announce/',views.announcement, name = "announcement"),
    path('makeAnnouncement/',views.makeAnnouncement, name = "makeAnnouncement"),

    # path('search/<int:id>/', views.search, name="search"),

    path('change-password/',views.change_password,name="change_password"),

    path('profile-update-student/', views.ProfileUpdateView, name='profile-update'),
    path('profile-update-faculty/', views.ProfileUpdateView2, name='profile-update2'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('reset_password/',auth_views.PasswordResetView.as_view(), name="rest_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    

]
