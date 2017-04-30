from django.shortcuts import render
from django.http import JsonResponse
from bs_app.models import Book, Rate, Category
from django.core import serializers
import json
# Create your views here.

def set_seen(request):
    request.user.profile.last
    return JsonResponse(request, 'bs_app/home.html',{'categories_books': categories_books, 'authors_books' : authors_books ,'latest_books': latest_books})

def get_notifications(request):
    qs = request.user.profile.notifications.all()[:5]
    new_notifications = request.user.profile.notifications.filter(id__gt=request.user.profile.last_notification_id).count()
    qs_json = serializers.serialize('json', qs)
    print(new_notifications)
    return JsonResponse({'data':qs_json, 'new_notifications': new_notifications})
