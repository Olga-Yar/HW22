from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contact, ProductDitailView, CategoryListView, \
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, BlogListView, BlogDitailView,\
    BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('category/', CategoryListView.as_view(), name='category_list'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDitailView.as_view(), name='product_item'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:post_slug>/', BlogDitailView.as_view(), name='blog_item'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:post_slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<slug:post_slug>/', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
