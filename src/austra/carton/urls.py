from django.urls import path
from django.conf.urls import include
from carton import views
urlpatterns = [
    path('', views.index, name='index'),
]