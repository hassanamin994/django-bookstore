from django.conf.urls import url, include
from django.contrib import admin
from .views.home import home
from .views import books, categories, authors, search, notifications

app_name="app"
urlpatterns = [
    url(r'^home/', home),
    url(r'^books/(?P<book_id>[0-9]+)/rate/(?P<new_rate>[0-9]+)$', books.book_rate, name="book_rate"),
    url(r'^books/(?P<book_id>[0-9]+)/wish$', books.book_wish, name="book_wish"),
    url(r'^books/(?P<book_id>[0-9]+)/read$', books.book_read, name="book_read"),
    url(r'^books/(?P<book_id>[0-9]+)$', books.book_detail, name="book_detail"),
    url(r'^books/', books.book_list,name="book_list"),

    url(r'^search/book/(?P<query>[a-zA-Z0-9]+)$', search.book_search, name="book_search"),
    url(r'^search/author/(?P<query>[a-zA-Z0-9]+)$', search.author_search, name="author_search"),

    url(r'^notifications/get', notifications.get_notifications, name="get_notifications"),
    url(r'^notifications/set/(?P<notification_id>[0-9]+)$', notifications.set_seen, name="set_notifications"),

    url(r'^authors/(?P<author_id>[0-9]+)/unsubscribe', authors.author_unsubscribe,name="author_unsubscribe"),
    url(r'^authors/(?P<author_id>[0-9]+)/subscribe', authors.author_subscribe,name="author_subscribe"),
    url(r'^authors/(?P<author_id>[0-9]+)', authors.author_detail,name="author_detail"),
    url(r'^authors/', authors.author_list,name="category_detail"),

    url(r'^categories/(?P<category_id>[0-9]+)/unsubscribe', categories.category_unsubscribe,name="category_unsubscribe"),
    url(r'^categories/(?P<category_id>[0-9]+)/subscribe', categories.category_subscribe,name="category_subscribe"),
    url(r'^categories/(?P<category_id>[0-9]+)', categories.category_detail,name="category_detail"),
    url(r'^categories/', categories.category_list,name="category_list"),
    url(r'^admin/', admin.site.urls),

]
