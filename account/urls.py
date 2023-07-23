from django.urls import path
from.import views

urlpatterns = [ 
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('home/', views.index, name='home'),
    path('logout/', views.logout, name='logout')
]
