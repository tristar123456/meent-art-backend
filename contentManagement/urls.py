from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('list', views.ItemList, name='items'),
    path('<uuid:id>', views.ItemDetail, name="item"),
    path('add', views.AddItem, name="add"),
    path('edit', views.EditItem, name="edit"),
    path('delete', views.DeleteItem, name="delete"),
]
