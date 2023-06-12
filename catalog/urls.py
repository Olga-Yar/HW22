from django.urls import path

from catalog.views import index, contact, post_card

urlpatterns = [
    path('', index),
    path('contact', contact),
    path('product/<int:pk>/', post_card)
]