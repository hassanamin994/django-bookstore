from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from bs_app.models import Category, Book
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

def category_detail(request, category_id):
    print(category_id)
    category = Category.objects.get(pk=category_id)
    books = Book.objects.filter(category=category_id)

    return render(request,'bs_app/category_detail.html',{'category':category,'books':books})



def category_subscribe(request, category_id):
    if request.user.profile.categories.filter(pk=category_id).count() == 0 :
        request.user.profile.categories.add(category_id)
    return redirect('/app/categories/'+str(category_id))


def category_unsubscribe(request, category_id):
    if request.user.profile.categories.filter(pk=category_id).count() == 1 :
        request.user.profile.categories.remove(category_id)
    return redirect('/app/categories/'+str(category_id))
