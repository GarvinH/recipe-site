from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('post/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('post/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('create-post/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('', views.RecipeListView.as_view(), name='recipe-home'),
]
