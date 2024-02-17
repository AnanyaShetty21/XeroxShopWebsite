from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.login, name="login"),
    path("pdflist/", views.ownerpdf, name="ownerpdf"),
    path("pdfliststudent/", views.studentpdf, name="studentpdf"),
    path("ownerorder/", views.ownerorder, name="ownerorder"),
    path("addpdf/", views.addPDF, name="addPDF"),


    

]
