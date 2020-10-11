from django.http import HttpResponse
from django.template import loader
from search.models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404


def index(request):
    template = loader.get_template('search/index.html')
    return HttpResponse(template.render(request=request))

def listing(request):
    product_list = Product.objects.filter(category_id=1).order_by('barcode')
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'paginate': True
    }
    return render(request, 'search/list_all.html', context)

def search(request):
    template = loader.get_template('search/form.html')
    return HttpResponse(template.render(request=request))   

def searching(request):
    query = request.GET.get('query')
    if not query:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(product_name__icontains=query)
    if not products.exists():
        message = "No Products found!"
    
    context = {
        'products': products
    }
    return render(request, 'search/search.html', context)