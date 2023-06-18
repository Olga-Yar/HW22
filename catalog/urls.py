from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contact, ProductDitailView, CategoryListView, \
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDitailView.as_view(), name='product_item'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
