# urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('control/', views.control_drone, name='control_drone'),
    path("index/", views.index, name='index'),
    path("video/", views.video_feed, name='video_feed'),
    # path('drone/status/', views.get_drone_status, name='drone_status'),
]
