
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_report', views.AContactView.as_view(), name='new_report'),
    path('neighborly/board/com/<int:product_id>', views.ComSetNeighborlyView.as_view() , name ='com'),
    path('update/<int:product_id>', views.IcreaseValueView.as_view(), name='update'),
    path('submissions', views.SubmissionsView.as_view() , name = 'zgloszenia'),
    path('announcements',views.AnnouncementsView.as_view(), name = 'ogloszenia'),
    path('neighborly', views.AddNeighborlyHelpView.as_view()),
    path('neighborly/board', views.BoardNeighborlyHelpView.as_view()),

    path('',views.IndexView.as_view(), name='report'),

]
