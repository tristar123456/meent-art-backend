from django.contrib import admin

# Register your models here.
from contentManagement.models import Item
from userManagement.models import Token


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    fields = ['date','title', 'text','image']

admin.site.register(Item, ItemAdmin)
admin.site.register(Token)