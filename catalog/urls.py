from django.urls import path



urlpatterns = [
    path('', index),
    path('contact', contact),
    path('product/<int:pk>/', post_card)
]