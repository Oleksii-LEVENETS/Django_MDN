from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('all_borrowed_books/', views.AllLoanedBooksListView.as_view(), name='all-borrowed-books'),

]
