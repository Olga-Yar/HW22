from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import ProductForm, BlogForm, VersionForm
from catalog.models import Category, Product, Blog, Version
from config import settings


# Create your views here.

class IndexView(generic.View):
    def get(self, request):

        if settings.CACHES_ENABLE:
            key = 'category_list'
            category_list = cache.get(key)
            if category_list is None:
                category_list = Category.objects.all()
                cache.set(key, category_list)
        else:
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
    version = Version

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            cat_id=self.kwargs.get('pk'),
        )

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)

    return render(request, 'catalog/contact.html')


class ProductDetailView(generic.DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST)
        else:
            context_data['formset'] = SubjectFormset()

        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    # def form_valid(self, form):
    #     formset = self.get_context_data()['formset']
    #     self.object = form.save()
    #
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #
    #     return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'
    redirect_field_name = 'next'

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner != self.request.user:
    #         raise Http404
    #     return self.object

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=0)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'
    redirect_field_name = 'next'


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        blog = super().get_object(queryset=queryset)
        blog.num_views += 1
        blog.save()
        return blog


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')
    slug_url_kwarg = 'slug'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_item')
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse('catalog:blog_item', kwargs={'slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
    slug_url_kwarg = 'slug'
