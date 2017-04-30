from django.shortcuts import render
from django.http import JsonResponse
from bs_app.models import Book, Rate, Category
from django.core import serializers
import json
# Create your views here.

def set_seen(request, notification_id):
    if request.user.profile.notifications.filter(pk=notification_id).exists():
        print(notification_id)
        print(request.user.profile.last_notification_id )
        request.user.profile.last_notification_id = notification_id
        request.user.profile.save()
        return JsonResponse({'status':True})
    else:
        return JsonResponse({'status':False})


def get_notifications(request):
    qs = request.user.profile.notifications.all().order_by('-id')[:5]
    for notific in qs :
        print(notific.id)
    new_notifications = request.user.profile.notifications.filter(id__gt=request.user.profile.last_notification_id).count()
    qs_json = serializers.serialize('json', qs)
    print(new_notifications)
    return JsonResponse({'data':qs_json, 'new_notifications': new_notifications})
