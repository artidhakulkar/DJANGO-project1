from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.


def contact(request):
     if request.method == "POST":
         email = request.POST.get('email', ''),
         name = request.POST.get('name', ''),
         city = request.POST.get('city', ''),
         phone = request.POST.get('phone', ''),
         address = request.POST.get('address', '')
         print(email, name, city, phone, address)
         contact = Contact(name=name, email=email, city=city, phone=phone, address=address)
         contact.save()

     return render(request, "app/contact.html")