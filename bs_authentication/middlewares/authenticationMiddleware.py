from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import re

class AuthenticationMiddleware(MiddlewareMixin):

    def process_request(self,request):
        #Prohibits user from accessing main app if not authenticated
        if re.match(r'/app/',request.path_info) :
            if not request.user or not request.user.is_authenticated():
                print('None Authorized')
                return HttpResponsePermanentRedirect('/auth/login')

        # Prohibits user from accessing login or registeration page if already authenticated
        if re.match(r'/auth/',request.path_info) :
            if request.user and request.user.is_authenticated():
                return HttpResponsePermanentRedirect('/app/books')

        return None
