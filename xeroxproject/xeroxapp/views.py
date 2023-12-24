from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ownerPDFlist, PDF, studentPDFlist, studentPDF, OwnerOrder, Credentials
from .addpdf import AddPDF
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def welcome(response):
    return render(response, "home.html", {})


def ownerpdf(response):
    p = ownerPDFlist.objects.get(name = "Notes")
    return render(response, "pdflist.html", {"p":p})

def studentpdf(response):
    p = studentPDFlist.objects.get(name = "Notes")
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("order"):
            for pdf in p.studentpdf_set.all():
                if response.POST.get(pdf.name) == "ordered":
                    s = pdf.Slno
                    n = pdf.name
                    p = pdf.price
                    owner_pdf_list, created = ownerPDFlist.objects.get_or_create(name="Orders")
                    o = OwnerOrder(Slno = s, name = n, price = p, completed = False, ownerPDFlist=owner_pdf_list)
                    o.save()
        
    return render(response, "pdfliststudent.html", {"p":p})



def ownerorder(response):
    p = ownerPDFlist.objects.get(name = "Orders")
    return render(response, "ownerorder.html", {"p":p})


def addPDF(response):
    if response.method == "POST":
        form = AddPDF(response.POST)
        print(response.POST)

        if form.is_valid():
            s = form.cleaned_data["Slno"]
            n = form.cleaned_data["name"]
            p = form.cleaned_data["price"]
            # Get or create ownerPDFlist (change the condition as needed)
            owner_pdf_list, created = ownerPDFlist.objects.get_or_create(name="Notes")
            student_pdf_list, created = studentPDFlist.objects.get_or_create(name="Notes")
            
            # Create a new PDF instance associated with the ownerPDFlist
            pdf = PDF(Slno=s, name=n, price=p, ownerPDFlist=owner_pdf_list)
            studentpdf = studentPDF(Slno=s, name=n, price=p, order=False, studentPDFlist=student_pdf_list)
            pdf.save()
            studentpdf.save()
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
