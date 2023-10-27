#IF THIS PAGE IS MODIFIED, REMEMBER TO EXCECUTE THE FOLLOWING COMMANDS IN PYTHON SHELL
#python manage.py makemigrations
#python manage.py migrate

from django.db import models

# Create your models here.

class ownerPDFlist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class PDF(models.Model):
    ownerPDFlist=models.ForeignKey(ownerPDFlist, on_delete=models.CASCADE) #use 'o.pdf_set.all()' to access all the pdfs present
    text=models.CharField(max_length=300)

    def __str__(self):
        return self.text
