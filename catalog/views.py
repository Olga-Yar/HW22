from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product


# Create your views here.
def index(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)

    return render(request, 'catalog/contact.html')


def post_card(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
