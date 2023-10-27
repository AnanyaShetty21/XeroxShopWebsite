from django.urls import path
from . import views

urlpatterns = [
    path("", views.owner, name="owner"),
    path("pdflist/", views.ownerpdf, name="ownerpdf"),
]
