from django.conf.urls import url, include
from django.contrib import admin
from .views.home import home
from .views import books
app_name="app"
urlpatterns = [
    url(r'^home/', home),
    url(r'^books/(?P<pk>[0-9]+)$', books.BookDetail.as_view(), name="book_detail"),
    url(r'^books/', books.BookList.as_view(),name="book_list"),
    url(r'^admin/', admin.site.urls),

]
