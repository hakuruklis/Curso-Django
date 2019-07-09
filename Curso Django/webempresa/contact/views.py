from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()
    return render(request,"contact/contact.html",{'form':contact_form})