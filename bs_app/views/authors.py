from django.shortcuts import render,get_list_or_404,get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from bs_app.models import Book, Rate, Author
from django.db.models import Avg


def author_list(request):
    authors = Author.objects.all()
    my_authors = Author.objects.filter(profile=request.user.id)
    return render(request,'bs_app/author_list.html', {'authors':authors,'my_authors':my_authors})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(authors=author_id)
    return render(request,'bs_app/author_detail.html',{'author':author,'books':books})
    pass

def author_subscribe(request, author_id):
    request.user.profile.authors.add(author_id)
    return redirect('/app/authors')

def author_unsubscribe(request, author_id):
    request.user.profile.authors.remove(author_id)
    return redirect('/app/authors')
