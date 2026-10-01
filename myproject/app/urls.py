from django.urls import path

from . import views

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("items/<int:pk>/edit/", views.item_edit, name="item_edit"),
    path("items/<int:pk>/delete/", views.item_delete, name="item_delete"),
    path("items/<int:pk>/toggle/", views.item_toggle, name="item_toggle"),
    path("api/items/", views.api_items, name="api_items"),
]
