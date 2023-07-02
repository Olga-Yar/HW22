from django import forms

from catalog.models import Product, Blog


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'about', 'price_lot', 'cat', 'image')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        if cleaned_data in stop_list:
            raise forms.ValidationError('Запрещенный продукт.')

        return cleaned_data

    def clean_about(self):
        cleaned_data = self.cleaned_data['about']
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        about = cleaned_data.split()

        for word in about:
            if word in stop_list:
                raise forms.ValidationError('Запрещенный продукт.')

        return cleaned_data


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'is_public')
