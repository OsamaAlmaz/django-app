from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


# Create your views here.
# render(request, template_name,context=None, status=None,using=None)
def home(request,*args, **kwargs):
    print(request.user)
    #return HttpResponse("Hello World!")
    return render(request, "home.html",{})

def contact(request, *args, **kwargs):
    my_context = {
        "my_text": "This is my context",
        "my_number": 123,
        "my_list": [312,213,4,5,6,7,8]
    }

    return render(request,"contact.html", my_context)