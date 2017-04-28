from django.conf.urls import url, include
from django.contrib import admin
from .views.home import home
from .views import books, categories, authors

app_name="app"
urlpatterns = [
    url(r'^home/', home),
    url(r'^books/(?P<book_id>[0-9]+)/rate/(?P<new_rate>[0-9]+)$', books.book_rate, name="book_detail"),
    url(r'^books/(?P<book_id>[0-9]+)/wish$', books.book_wish, name="book_detail"),
    url(r'^books/(?P<book_id>[0-9]+)/read$', books.book_read, name="book_detail"),
    url(r'^books/(?P<book_id>[0-9]+)$', books.book_detail, name="book_detail"),
    url(r'^books/', books.book_list,name="book_list"),

    url(r'^authors/(?P<author_id>[0-9]+)/unsubscribe', authors.author_unsubscribe,name="category_detail"),
    url(r'^authors/(?P<author_id>[0-9]+)/subscribe', authors.author_subscribe,name="category_detail"),
    url(r'^authors/(?P<author_id>[0-9]+)', authors.author_detail,name="category_detail"),
    url(r'^authors/', authors.author_list,name="category_detail"),

    url(r'^categories/(?P<category_id>[0-9]+)/unsubscribe', categories.category_unsubscribe,name="category_detail"),
    url(r'^categories/(?P<category_id>[0-9]+)/subscribe', categories.category_subscribe,name="category_detail"),
    url(r'^categories/(?P<category_id>[0-9]+)', categories.category_detail,name="category_detail"),
    url(r'^categories/', categories.category_list,name="category_list"),
    url(r'^admin/', admin.site.urls),

]
