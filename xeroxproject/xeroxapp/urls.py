from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("pdflist/", views.ownerpdf, name="ownerpdf"),
    path("pdfliststudent/", views.studentpdf, name="studentpdf"),
    path("ownerorder/", views.ownerorder, name="ownerorder"),
    path("addpdf/", views.addPDF, name="addPDF"),
    path("login/", views.login, name="login")

]
