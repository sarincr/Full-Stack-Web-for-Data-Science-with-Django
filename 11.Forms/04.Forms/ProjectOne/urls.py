
from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.indexone),
    path("results", views.result),
]
