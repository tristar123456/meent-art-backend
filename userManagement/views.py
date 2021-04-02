import json

from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponseForbidden
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_exempt

from contentManagement.views import checkAccess
from userManagement.models import Token


@csrf_exempt
def Login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        try:
            token = Token.objects.get(user=user)
            if token is not None:
                print(token.date < timezone.now())
                if token.date < timezone.now():
                    token.delete()
                    token = Token(user=user)
            else:
                token = Token(user=user)
        except Token.DoesNotExist:
            token = Token(user=user)
        token.save()
        return JsonResponse(token.api_token, safe=False)
    else:
        return HttpResponseForbidden()


@csrf_exempt
def Logout(request):
    allowed = checkAccess(request)
    if allowed:
        auth_header = request.headers.get('Authorization')
        token = auth_header.split(" ")[1]
        token = Token.objects.get(api_token__exact=token)
        print(token, ' was deleted!')
        token.delete()
    return JsonResponse(True, safe=False)
