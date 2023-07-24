from catalog.models import Category

def get_category():
    category_list = Category.objects.all()
    return category_list