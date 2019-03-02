from django.urls import path
from . views import login, index, logout, register, profile_page, update_profile

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('',index),
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    path('profile/', profile_page),
    path('update_profile', update_profile)
]