from django.shortcuts import render
from django.http import JsonResponse
from bs_app.models import Book, Rate, Category
# Create your views here.

def home(request):
    my_categories = []
    my_authors = []

    # getting list of user's categories ids
    for category in request.user.profile.categories.all():
        my_categories.append(category.id)
    #getting list for user's authors ids
    for author in request.user.profile.authors.all():
        my_authors.append(author.id)

    categories_books = Book.objects.filter(category__in=my_categories)
    authors_books = Book.objects.filter(authors__in=my_authors)
    latest_books =  Book.objects.all().order_by('-id')[:10]
    return render(request, 'bs_app/home.html',{'categories_books': categories_books, 'authors_books' : authors_books ,'latest_books': latest_books})
