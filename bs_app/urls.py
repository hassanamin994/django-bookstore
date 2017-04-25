from django.conf.urls import url, include
from django.contrib import admin
from .views.home import home
from .views import books
from .views import categories
app_name="app"
urlpatterns = [
    url(r'^home/', home),
    url(r'^books/(?P<pk>[0-9]+)$', books.BookDetail.as_view(), name="book_detail"),
    url(r'^books/', books.BookList.as_view(),name="book_list"),

    url(r'^categories/(?P<category_id>[0-9]+)', categories.category_detail,name="category_detail"),
    url(r'^categories/', categories.category_list,name="category_list"),
    url(r'^admin/', admin.site.urls),

]
