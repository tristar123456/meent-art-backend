import json
import os
import uuid

from PIL.Image import Image
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from contentManagement.models import Item
from userManagement.models import Token


import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate(os.environ.get('PWD')+"/meent-art-pinboard-90a20008cad4.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://meent-art-pinboard.appspot.com'
})

_bucket = storage.bucket()

# from google.cloud import storage
#
# # Instantiates a client
# storage_client = storage.Client()
#
# # The name for the new bucket
# bucket_name = "images"
#
# # Creates the new bucket
# _bucket = storage_client.create_bucket(bucket_name)
#
# print("Bucket {} created.".format(_bucket.name))

def ItemList(request):
    item_list = Item.objects.all()
    json_item_list = [jsonItem(item, request) for item in item_list]
    return JsonResponse(json_item_list, safe=False)


def ItemDetail(request, id):
    try:
        item = Item.objects.get(id__exact=id)
        json_item = jsonItem(item, request)
    except Item.DoesNotExist:
        raise Http404('Item does not exist')
    return JsonResponse(json_item)


def jsonItem(item, request):
    try:
        imgLink = request.build_absolute_uri(item.image.url)
    except ValueError:
        imgLink = item.image_url if item.image_url is not None else ''

    json_item = {
        'id': str(item.id),
        'date': str(item.date) if item.date is not None else '',
        'title': item.title if item.title is not None else '',
        'text': item.text if item.text is not None else '',
        'imgLink': imgLink
    }
    return json_item


def checkAccess(request):
    auth_header = request.headers.get('Authorization')
    if (auth_header == None):
        return False
    else:
        try:
            token = auth_header.split(" ")[1]
            if (len(token) == 36):
                if Token.objects.get(api_token__exact=token) is not None:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


def parseBody(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body


@csrf_exempt
def AddItem(request):
    if checkAccess(request):
        body = parseBody(request)['addItem']
        try:
            title = body['title']
        except:
            title = ''
        try:
            text = body['text']
        except:
            text = ''
        try:
            image_url = body['imgLink']
        except:
            image_url = ''
        try:
            image = _bucket.blob(str(uuid.uuid4())[:12]).upload_from_string((body['image']))
        except:
            image = None

        Item.objects.create(
            title=title,
            text=text,
            image_url=image_url,
            image=image
        )

        return JsonResponse(True, safe=False)
    else:
        return HttpResponseForbidden()


@csrf_exempt
def EditItem(request):
    if checkAccess(request):
        body = parseBody(request)['editedItem']
        edited_item = Item.objects.get(id__exact=body['id'])
        try:
            edited_item.title = body['title']
        except:
            pass
        try:
            edited_item.text = body['text']
        except:
            pass
        try:
            edited_item.image_url = body['imgLink']
        except:
            pass
        try:
            edited_item.image = decode_base64_file(body['image'])
        except:
            pass
        edited_item.save()
        return JsonResponse(True, safe=False)
    else:
        return HttpResponseForbidden()

def decode_base64_file(data):

    def get_file_extension(file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

    from django.core.files.base import ContentFile
    import base64
    import six
    import uuid

    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension, )

        return ContentFile(decoded_file, name=complete_file_name)


@csrf_exempt
def DeleteItem(request):
    if checkAccess(request):
        body = parseBody(request)['deleteItem']
        delete_item = Item.objects.get(id__exact=body['id'])
        delete_item.delete()
        return JsonResponse(True, safe=False)
    else:
        return HttpResponseForbidden()


