from django.shortcuts import render , redirect
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def uploade(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        sku = data.get("sku")
        description = data.get("description")
        photo = request.FILES.get("photo")
        #color = data.get("color")
        size = data.get("size")
        price = data.get("price")
        stock = data.get("stock")
        
        
        Product.objects.create(
            name= name,
            sku=sku,
            description = description,
            photo =photo,
            #color = color,
            size = size ,
            price = price ,
            stock = stock ,
            
        )
        return redirect('/productlist/')
        
        
    return render(request,"uploade.html")



def deleteproduct(request , id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('/productlist')

def productlist(request):
    data = Product.objects.all()
    if request.GET.get('search'):
        data = data.filter(
            name__icontains=request.GET.get('search')
        )
    
    Paginat = Paginator(data , 5 )
    page_number = request.GET.get('page')
    datafinal = Paginat.get_page(page_number)
    totolpage = datafinal.paginator.num_pages
    
    
    context = {
        'data':datafinal,
        'lastpage':totolpage,
        'totalpagelist':[n+1 for n in range(totolpage)],
    }
    
    return render(request, "productlist.html",context)



def updateproduct(request , id):
    queryset = Product.objects.get(id=id)
    if request.method=="POST":
        data= request.POST
        name = data.get('name')
        sku = data.get('sku')
        description = data.get('description')
        photo = request.FILES.get('photo')
        size =data.get('size')
        price = data.get('price')
        stock = data.get('stock')
        
        queryset.name = name
        queryset.sku = int(sku)
        queryset.description =description
        queryset.size = size
        queryset.price = price
        queryset.stock = stock
        queryset.save()
        if photo:
            queryset.photo = photo
            queryset.save()
            return redirect('/productlist/')
        
        return redirect('/productlist/')
    
    context = {
        'Product':queryset
    }
    return render(request,"update.html",context)