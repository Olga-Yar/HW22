from django import forms

from catalog.models import Product, Blog


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'about', 'price_lot', 'cat', 'image')


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'is_public')
