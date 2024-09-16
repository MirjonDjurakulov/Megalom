from django.urls import path

from base import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.index, name='sort')
]