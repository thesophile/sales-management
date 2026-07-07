from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from .models import Product, Category

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    selected_category = request.GET.get("category")
    if selected_category:
        products = products.filter(category_id=selected_category)

    return render(request, 'user_section/index.html', {
        "products": products,
        "categories": categories,
        "selected_category": selected_category,
    })