from django.shortcuts import render
from . models import Detail

# Create your views here.
def home(request):
    website=Detail.objects.all()
    return render(request,"home.html",{'website':website})

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")