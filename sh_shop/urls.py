from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('male/', views.male, name="male"),
    path('female/', views.female, name="female"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('category/<slug>/', views.category, name='category'),
    path('gender/<str:gender>/', views.gender_filter, name='gender'),
    path('gender/<str:gender>/type/<str:type>/', views.gender_type_filter, name='gender_type'),
    path('search/', views.search, name='search'),
    path('mypage/', views.mypage, name='mypage'),
]