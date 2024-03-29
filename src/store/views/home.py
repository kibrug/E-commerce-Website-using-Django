from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('store:homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

def home_View(request):
    
    return render(request,'home.html')

def search_View(request):
    query_dict = request.GET
    query = query_dict.get("q")
    print(query)
    searchdata = None
    #nodata = "No Search Results"
    if query is not None:
        searchdata = Products.objects.get(name__icontains=query)
    context ={"searchdata":searchdata}
        
    return render(request, 'search.html',context )
def search_View_Send(request):
    query_dict = request.GET
    query = query_dict.get("q")
    print(query)
    searchdata = None
    #nodata = "No Search Results"
    if query is not None:
        searchdata = Products.objects.get(name__icontains=query)
    context ={"searchdata":searchdata}
        
    return render(request, 'searchget.html',context )