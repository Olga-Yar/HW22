from django import forms

from catalog.models import Product, Blog, Version


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):

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


class VersionForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'is_active')


class BlogForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'is_public')
