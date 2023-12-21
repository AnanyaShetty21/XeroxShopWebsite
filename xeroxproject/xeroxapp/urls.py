from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("pdflist/", views.ownerpdf, name="ownerpdf"),
    path("addpdf/", views.addPDF, name="addPDF"),

]
