#IF THIS PAGE IS MODIFIED, REMEMBER TO EXCECUTE THE FOLLOWING COMMANDS IN PYTHON SHELL
#python manage.py makemigrations xeroxapp
#python manage.py migrate

from django.db import models

# Create your models here.

class ownerPDFlist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    #Meta data for ownerPDFlist
    #Else the display name in the admin dashboard will be "Owner pd flists"
    class Meta:
        verbose_name_plural="ownerPDFlist"
    
class PDF(models.Model):
    ownerPDFlist=models.ForeignKey(ownerPDFlist, on_delete=models.CASCADE) #use 'o.pdf_set.all()' to access all the pdfs present
    Slno=models.IntegerField()
    name=models.CharField(max_length=300)
    price = models.IntegerField()


    def __str__(self):
        return f"{self.Slno} - {self.name} - {self.price}"
    
    #Meta data for PDF
    #Else the display name in the admin dashboard will be "Pdfs"
    class Meta:
        verbose_name="PDF"
        verbose_name_plural="PDFs"


class CredentialList(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "CredentialList"
        
    
class Credentials(models.Model):
    CredentialList=models.ForeignKey(CredentialList, on_delete=models.CASCADE)
    regno = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.regno
    
    class Meta:
        verbose_name_plural = "Credentials"