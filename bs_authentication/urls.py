"""bs_authentication URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^login/', views.login_view),
    url(r'^register/',views.register_view),
    url(r'^logout/',views.logout_view),
]
