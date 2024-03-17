
from django.contrib import admin
from django.urls import path
from appone import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.indexone),
    path("logins", views.logins),
    path("signup", views.signup),
    path("data", views.data),
]
