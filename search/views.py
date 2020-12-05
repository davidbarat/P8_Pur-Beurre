import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import UserForm, RegisterForm
from search.models import Product, Category, User, DetailProduct, Substitute


def index(request):
    template = loader.get_template("search/index.html")
    return HttpResponse(template.render(request=request))


@login_required()
def search(request):
    template = loader.get_template("search/form.html")
    return HttpResponse(template.render(request=request))


# @login_required()
def searching(request):
    query = request.GET.get("query")
    product_nutriscore = ""
    product_category = 1
    product_picture_path = ""
    message = ""
    products = ""
    product_query_data = ""
    product_query_json = {}

    if not query:
        message = "Remplissez le champ de recherche"
    else:
        product_query_data = serializers.serialize(
            "json",
            Product.objects.filter(product_name__icontains=query)[:1],
            fields=("nutriscore_grade", "category", "picture_path"),
        )
        product_query_json = json.loads(product_query_data)
        if product_query_json:
            for products in product_query_json:
                product_nutriscore = products["fields"]["nutriscore_grade"]
                product_category = products["fields"]["category"]
                product_picture_path = products["fields"]["picture_path"]
        else:
            message = (
                "Le produit n'a pas été trouvé, veuillez effectuer une autre recherche"
            )

    substitutes = Product.objects.filter(
        nutriscore_grade__lt=product_nutriscore
    ).filter(category_id__exact=product_category)
    paginator = Paginator(substitutes, 9)
    page = request.GET.get("page")
    try:
        substitutes = paginator.page(page)
    except PageNotAnInteger:
        substitutes = paginator.page(1)
    except EmptyPage:
        substitutes = paginator.page(paginator.num_pages)

    context = {
        "substitutes": substitutes,
        "product_picture_path": product_picture_path,
        "query": query,
        "paginate": True,
        "message": message,
    }
    return render(request, "search/list.html", context)


def login2(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data:
                post = User()
                # post.username = request.POST.get('username')
                post.email = request.POST.get("email")
                # post.first_name = request.POST.get('first_name')
                # post.last_name = request.POST.get('last_name')
                post.password = request.POST.get("password")
                post.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/search/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, "search/profile.html", {"form": form})


def logout2(request):

    logout(request)

    return redirect(reverse("index"))


def register(request):

    registered = False
    if request.method == "POST":
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()
    return render(
        request, "search/registration.html", {"user_form": user_form, "registered": registered}
    )


def profile(request, username=None):

    if username:
        post_owner = get_object_or_404(User, username=username)

    else:
        post_owner = request.user

    args1 = {
        "post_owner": post_owner,
    }
    return render(request, "search/profile.html", args1)


def mentions(request):
    template = loader.get_template("search/mentions.html")
    return HttpResponse(template.render(request=request))


@login_required()
def detail(request, barcode):
    # products = get_object_or_404(Product, pk=barcode)
    products = Product.objects.filter(barcode__icontains=barcode)[:1]
    detail_products = DetailProduct.objects.filter(id_id__barcode__icontains=barcode)[
        :1
    ]
    for product in products:
        product_dict = {
            "product_name": product.product_name,
            "product_grade": product.nutriscore_grade,
            "product_pic": product.picture_path,
            "product_url": product.url,
            "small_product_pic": product.small_picture_path,
        }

    for detail_product in detail_products:
        detail_products_dict = {
            "energy_100g": detail_product.energy_100g,
            "energy_unit": detail_product.energy_unit,
            "sugars_100g": detail_product.sugars_100g,
            "fiber_100g": detail_product.fiber_100g,
            "salt_100g": detail_product.salt_100g,
        }

    context = {**product_dict, **detail_products_dict}

    return render(request, "search/detail.html", context)


@login_required()
def myproducts(request):

    user_email = None
    list_products = []
    if request.user.is_authenticated:
        user_email = request.user.email

    mysubstitute_product_data = serializers.serialize(
        "json",
        Substitute.objects.filter(user_email__exact=user_email),
        fields=("substitute_id"),
    )
    mysubstitute_product_json = json.loads(mysubstitute_product_data)
    # return HttpResponse(mysubstitute_product_data)
    for product in mysubstitute_product_json:
        list_products.append(product["fields"]["substitute_id"])
        # myproducts_list.append(Product.objects.filter(
        #     product_id__exact=element))
    # return HttpResponse(list_products)

    myproducts = Product.objects.filter(product_id__in=list_products).order_by(
        "product_id"
    )

    paginator = Paginator(myproducts, 9)
    page = request.GET.get("page")
    try:
        myproducts = paginator.page(page)
    except PageNotAnInteger:
        myproducts = paginator.page(1)
    except EmptyPage:
        myproducts = paginator.page(paginator.num_pages)

    context = {"myproducts": myproducts, "paginate": True}
    return render(request, "search/myproducts.html", context)


@login_required()
def save(request, id):

    user_email = None
    product_obj = Product.objects.get(product_id__exact=id)

    if request.user.is_authenticated:
        user_email = request.user.email

    substitute_obj = Substitute.objects.create(
        user_email=user_email, substitute_id=product_obj
    )
    try:
        substitute_obj.save()
        # return HttpResponse("SaveOK")
        message = "Le produit " + product_obj.product_name + " a bien été enregistré"
        context = {"message": message}
        return render(request, "search/myproducts.html", context)

    except:
        # return HttpResponse("SaveError")
        message = (
            "Il y a eu un problème lors de l enregistrement du produit "
            + product_obj.product_name
        )
        context = {"message": message}
        return render(request, "search/myproducts.html", context)
