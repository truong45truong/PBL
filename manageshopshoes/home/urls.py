from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage,name='home'),
    path('info-account',views.myAccountPage,name='myaccount'),
]