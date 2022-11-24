from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.Index),
    path("handlecredentials",views.handlecredentials,name="handlecredentials"),
    path("processed",views.processed,name="processed"),
    path("ERR",views.ERR,name="ERR")
]
