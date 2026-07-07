from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

from user_section.models import Product, Category


@staff_member_required(login_url='admin_login')
def admin(request):
    products = Product.objects.all()
    return render(request, 'admin_side/admin.html', {'products': products})




@staff_member_required(login_url='admin_login')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("index")

@staff_member_required(login_url='admin_login')
def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            Title=request.POST["Title"],
            amount=request.POST["amount"],
            image=request.FILES["image"],
            category_id=request.POST["category"],
        )
        return redirect("admin")

    categories = Category.objects.all()
    return render(request, "admin_side/add.html", {"categories": categories})



@staff_member_required(login_url='admin_login')
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.Title = request.POST["Title"]
        product.amount = request.POST["amount"]
        product.category_id = request.POST["category"]
        if request.FILES.get("image"):
            product.image = request.FILES["image"]
        product.save()
        return redirect("admin")

    categories = Category.objects.all()
    return render(request, "admin_side/edit_product.html", {"product": product, "categories": categories})


@staff_member_required(login_url='admin_login')
def category_list(request):
    categories = Category.objects.all()
    return render(request, "admin_side/category_list.html", {"categories": categories})


@staff_member_required(login_url='admin_login')
def add_category(request):
    if request.method == "POST":
        Category.objects.create(name=request.POST["name"])
        return redirect("category_list")
    return render(request, "admin_side/add_category.html")


@staff_member_required(login_url='admin_login')
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.name = request.POST["name"]
        category.save()
        return redirect("category_list")
    return render(request, "admin_side/edit_category.html", {"category": category})


@staff_member_required(login_url='admin_login')
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("category_list")