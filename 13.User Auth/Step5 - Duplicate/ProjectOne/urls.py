
from django.contrib import admin
from django.urls import path
from appone import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
