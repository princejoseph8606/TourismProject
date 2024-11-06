from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('vendor/signup/', views.vendor_signup, name='vendor_signup'),
    path('vendor/login/', views.vendor_login, name='vendor_login'),
    path('vendor_home/', views.vendor_home, name='vendor_home'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('edit_package/<int:package_id>/', views.edit_package, name='edit_package'),
    path('vendor/logout/', views.vendor_logout, name='vendor_logout'),

    path('user/signup/', views.user_signup, name='user_signup'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user/logout/', views.user_logout, name='user_logout'),
]
