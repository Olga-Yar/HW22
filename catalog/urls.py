from django.urls import path

from catalog.views import index, contact, post_card

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('product/<int:pk>/', post_card)
]