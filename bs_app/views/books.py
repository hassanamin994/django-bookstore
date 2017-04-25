from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from bs_app.models import Book
from django.views.generic import ListView, DetailView
# Create your views here.

# @require_http_methods(['GET'])
# def book_list(request):
#     books = get_list_or_404(Book)
#     for book in books:
#         print( book.title)
#
#     return HttpResponse('books list')

def book_list(request):
    books = Book.objects.all()

    return render(request, 'bs_app/book_list.html',{'object_list': books })

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, 'bs_app/book_detail.html',{'object': book })
