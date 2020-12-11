from ordersManage.models import Article
from ordersManage.forms import ContactForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def search_products(request):

    return render(request, "search_products.html")

def search(request):

    if request.GET["prd"]:
        #message = "Article found: %r" %request.GET["prd"]

        product = request.GET["prd"]

        if len(product)>20:
            message = "Article is too long."

        else:
            articles = Article.objects.filter(name__icontains=product)
            return render(request, "result_search.html", {"articles":articles, "query":product})
    
    else:
        message="You didnt insert anything."

    return HttpResponse(message)

# def contact(request):

#    if request.method == "POST":

#        subject = request.POST["subject"]
#        message = request.POST["messageContact"] + " " + request.POST["email"]
#        email_from = settings.EMAIL_HOST_USER

#       recipient_list = ["antonio.hh7@gmail.com"]

#        send_mail(subject, message, email_from, recipient_list)


#        return render(request, "thanks.html")

#    return render(request, "contact.html")

#Using API FORMS

def contact(request):

    if request.method == "POST":

        myForm = ContactForm(request.POST)

        if myForm.is_valid():

            cleanFormData = myForm.cleaned_data

            send_mail(cleanFormData['subject'], cleanFormData['email'], cleanFormData.get('email',''), ['antonio.hh7@gmail.com'],)

            return render(request, "thanks.html")
    
    else:

        myForm = ContactForm()
    
    return render(request, "contact_form.html", {"form" : myForm})