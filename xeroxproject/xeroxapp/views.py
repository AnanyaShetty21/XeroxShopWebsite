from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ownerPDFlist, PDF, Credentials
from .addpdf import AddPDF
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def welcome(response):
    return render(response, "home.html", {})


"""def ownerpdf(response):
    ls = ownerPDFlist.objects.get(name = "Notes") #id=1
    pdf = ls.pdf_set.all()
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>"%(ls.name,str(pdf.text)))"""


def ownerpdf(response):
    p = ownerPDFlist.objects.get(name = "Notes")
    return render(response, "pdflist.html", {"p":p})


def addPDF(response):
    if response.method == "POST":
        form = AddPDF(response.POST)

        if form.is_valid():
            s = form.cleaned_data["Slno"]
            n = form.cleaned_data["name"]
            p = form.cleaned_data["price"]
            # Get or create ownerPDFlist (change the condition as needed)
            owner_pdf_list, created = ownerPDFlist.objects.get_or_create(name="Notes")
            
            # Create a new PDF instance associated with the ownerPDFlist
            pdf = PDF(Slno=s, name=n, price=p, ownerPDFlist=owner_pdf_list)
            pdf.save()
        return HttpResponseRedirect("/addpdf")
    else:
        form = AddPDF()
    return render(response, "addpdf.html", {"form":form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            regno = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = Credentials.objects.filter(regno=regno, password=password).first()
            

            if user:
                return HttpResponseRedirect('/pdflist')
            else:
                return render(request, 'login.html', {'error_message' : 'Invalid credentials. Please try again.'})

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
