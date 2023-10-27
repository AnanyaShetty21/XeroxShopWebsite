from django.shortcuts import render
from django.http import HttpResponse
from .models import ownerPDFlist, PDF


# Create your views here.


def owner(response):
    return HttpResponse("<h1>Owner's webpage</h1>")
#def ownerpdf(response):
 #   ls = ownerPDFlist.objects.get(name = "Owner\'s PDFs") #id=1
  #  pdf = ls.pdf_set.all()
   # return HttpResponse("<h1>%s</h1><br></br><p>%s</p>"%(ls.name,str(pdf.text)))


def ownerpdf(response):
    try:
        ls = ownerPDFlist.objects.get(name="Owner's PDFs")
        pdfs = ls.pdf_set.all()
        
        output = f"<h1>{ls.name}</h1>"
        
        if pdfs:
            for pdf in pdfs:
                output += f"<p>{pdf.text}</p>"
        else:
            output += "<p>No PDFs found.</p>"
        
        return HttpResponse(output)
    except ownerPDFlist.DoesNotExist:
        return HttpResponse("Owner's PDFs list does not exist.")
