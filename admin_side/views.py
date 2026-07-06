from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from user_section.models import Product

def admin(request):
    products = Product.objects.all()
    return render(request, 'admin_side/admin.html', {'products': products})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.Title = request.POST["Title"]
        product.amount = request.POST["amount"]
        product.save()
        return redirect("index")

    return render(request, "user_section/edit.html", {"product": product})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("index")


def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            Title=request.POST["Title"],
            amount=request.POST["amount"],
            image=request.FILES["image"],
        )
        return redirect("admin")

    return render(request, "admin_side/add.html")