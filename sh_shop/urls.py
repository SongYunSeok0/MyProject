from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('category/<slug>/', views.category, name='category'),
]