from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from bs_app.models import Category
from django.views.generic import ListView, DetailView
# Create your views here.

# @require_http_methods(['GET'])
# def book_list(request):
#     books = get_list_or_404(Book)
#     for book in books:
#         print( book.title)
#
#     return HttpResponse('books list')

def category_list(request):
    categories = Category.objects.all()
    my_categories = Category.objects.filter(profile=request.user.id)
    return render(request,'bs_app/category_list.html', {'categories':categories,'my_categories':my_categories})
