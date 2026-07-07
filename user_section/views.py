from django.shortcuts import render, redirect, get_object_or_404
    
from .models import Product, Category, Enquiry

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


def enquiry_form(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        Enquiry.objects.create(
            product=product,
            name=request.POST["name"],
            address=request.POST["address"],
            quantity=request.POST["quantity"],
            mobile_number=request.POST["mobile_number"],
        )
        return redirect("enquiry_success")

    return render(request, "user_section/enquiry_form.html", {"product": product})


def enquiry_success(request):
    return render(request, "user_section/enquiry_success.html")