from django.shortcuts import render,get_list_or_404,get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from bs_app.models import Book, Rate
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

def book_list(request):
    books = Book.objects.all()

    return render(request, 'bs_app/book_list.html',{'object_list': books })

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    rate = Rate.objects.filter(book=book_id)
    if len(rate) == 1 :
        rate = rate[0]
    rates_list = map(str, range(1,10))
    average_rate =book.rate_set.aggregate(Avg('rate'))['rate__avg']
    return render(request, 'bs_app/book_detail.html',{'object': book, 'properties': rate, 'rate_list':rates_list, 'average_rating': average_rate})

def book_rate(request, book_id, new_rate):
    rate = get_rate(request.user.profile, book_id)
    rate.rate = str(new_rate)
    rate.save()
    return redirect('/app/books/'+str(book_id))

def book_wish(request, book_id):
    rate = get_rate(request.user.profile, book_id)
    rate.state='wish'
    rate.save()
    return redirect('/app/books/'+str(book_id))

def book_read(request, book_id):
    rate = get_rate(request.user.profile, book_id)
    rate.state='read'
    rate.save()
    return redirect('/app/books/'+str(book_id))

#if user didnt rate book before, create an entity for him
def get_rate(profile, book_id):
    if len(Rate.objects.filter(book=book_id)) == 0:
        rate = create_rate(profile, book_id)
    else:
        rate = Rate.objects.get(book=book_id)
    return rate

def create_rate(profile, book_id):
    return Rate.objects.create(profile=profile, book= Book.objects.get(pk=book_id))
