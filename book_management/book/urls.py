from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('book_list/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('book_list/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('search_books/', views.search_books, name='search_books'),
]