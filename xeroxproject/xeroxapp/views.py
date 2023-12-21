from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ownerPDFlist, PDF
from .addpdf import AddPDF


# Create your views here.


def welcome(response):
    return render(response, "xeroxapp/home.html", {})


"""def ownerpdf(response):
    ls = ownerPDFlist.objects.get(name = "Notes") #id=1
    pdf = ls.pdf_set.all()
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>"%(ls.name,str(pdf.text)))"""


def ownerpdf(response):#This block of code will be modified once the template is created
    try:
        ls = ownerPDFlist.objects.get(name="Notes")
        pdfs = ls.pdf_set.all()
        
        output = f"<h1>{ls.name}</h1>"
        
        if pdfs:
            output += "<h3>Sl no.   PDF     Price</h3>" 
            for pdf in pdfs:
                output += f"<p>{pdf.Slno}   {pdf.name}  {pdf.price}</p>"
        else:
            output += "<p>No notes found.</p>"
        
        return HttpResponse(output)
    except ownerPDFlist.DoesNotExist:
        return HttpResponse("Notes does not exist.")


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
    return render(response, "xeroxapp/addpdf.html", {"form":form})
