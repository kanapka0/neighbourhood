
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_report', views.AContactView.as_view(), name='new_report'),
    path('',views.IndexView.as_view(), name='report'),

]
