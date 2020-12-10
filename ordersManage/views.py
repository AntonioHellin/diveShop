from ordersManage.models import Article
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def search_products(request):

    return render(request, "search_products.html")

def search(request):

    if request.GET["prd"]:
        #message = "Article found: %r" %request.GET["prd"]

        product = request.GET["prd"]

        articles = Article.objects.filter(name__icontains=product)

        return render(request, "result_search.html", {"articles":articles, "query":product})
    
    else:
        message="You didnt insert anything."

    return HttpResponse(message)