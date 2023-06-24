from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Category, Product, Blog


# Create your views here.
def index(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


class CategoryListView(generic.ListView):
    model = Category


class ProductListView(generic.ListView):
    model = Product


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)

    return render(request, 'catalog/contact.html')


class ProductDitailView(generic.DetailView):
    model = Product


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'about', 'price_lot', 'cat')
    success_url = reverse_lazy('product_list')


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ('name', 'about', 'price_lot', 'cat')
    success_url = reverse_lazy('product_list')


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class BlogListView(generic.ListView):
    model = Blog


class BlogDitailView(generic.DetailView):
    model = Blog
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        blog = super().get_object(queryset=queryset)
        blog.num_views += 1
        blog.save()
        return blog


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('blog_list')
    slug_url_kwarg = 'post_slug'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('blog_list')
    slug_url_kwarg = 'post_slug'


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
    slug_url_kwarg = 'post_slug'
