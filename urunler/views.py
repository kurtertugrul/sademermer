
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, CatFloor, Floor
from insaat.views import Communicate

floor_categories = CatFloor.objects.all()
communication_info = Communicate.objects.first()
def category(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    selected_category_id = request.GET.get('category_id')
    
    # If a category ID is provided, fetch the category object
    selected_category = None
    if selected_category_id:
        selected_category = get_object_or_404(Category, id=selected_category_id)
    
    return render(request, 'stand.html', {'categories': categories,
                                          'products': products,
                                          'selected_category': selected_category,
                                          'communication_info': communication_info,
                                          'floor_categories':floor_categories })
    

categories = Category.objects.all()


def category_floor(request):
    floor_categories = CatFloor.objects.all()
    floors = Floor.objects.all()
    selected_category_id = request.GET.get('category_id')

    # Eğer bir kategori ID'si sağlanıyorsa, ilgili kategori objesini al
    selected_category = None
    if selected_category_id:
        selected_category = get_object_or_404(CatFloor, id=selected_category_id)

    return render(request, 'floor.html', {'floor_categories': floor_categories,
                                           'floors': floors,
                                           'selected_category': selected_category,
                                           'communication_info': communication_info,
                                           'categories': categories,
                                           })

