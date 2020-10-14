from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from search.models import Product, Category, User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .forms import AccountForm


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

def create_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data:
                post = User()
                form.username = request.POST.get('username')
                form.email = request.POST.get('email')
                form.first_name = request.POST.get('first_name')
                form.last_name = request.POST.get('last_name')
                form.password = request.POST.get('password')
                post.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/search/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AccountForm()

    return render(request, 'create_user.html', {'form': form}) 