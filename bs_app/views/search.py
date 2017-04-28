from django.shortcuts import render,get_list_or_404,get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from bs_app.models import Book, Rate, Author
from django.views.generic import ListView, DetailView
from django.db.models import Avg
# Create your views here.

# @require_http_methods(['GET'])
# def book_list(request):
#     books = get_list_or_404(Book)
#     for book in books:
#         print( book.title)
#
#     return HttpResponse('books list')

def book_search(request, query):
    books = Book.objects.filter(title__icontains=query)

    return render(request, 'bs_app/search.html',{'search_type':'book', 'books': books })

def author_search(request, query):
    authors = Author.objects.filter(name__icontains=query)
    my_authors = Author.objects.filter(profile=request.user.id)
    return render(request,'bs_app/search.html', {'search_type':'author', 'authors':authors,'my_authors':my_authors})
