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



class studentPDFlist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    #Meta data for studentPDFlist
    #Else the display name in the admin dashboard will be "Student pd flists"
    class Meta:
        verbose_name_plural="studentPDFlist"
    
class studentPDF(models.Model):
    studentPDFlist=models.ForeignKey(studentPDFlist, on_delete=models.CASCADE) #use 'o.pdf_set.all()' to access all the pdfs present
    Slno=models.IntegerField()
    name=models.CharField(max_length=300)
    price = models.IntegerField()
    order = models.BooleanField()


    def __str__(self):
        return f"{self.Slno} - {self.name} - {self.price} - {self.order}"
    
    #Meta data for studentPDF
    #Else the display name in the admin dashboard will be "studentPdfs"
    class Meta:
        verbose_name="studentPDF"
        verbose_name_plural="studentPDFs"


class OwnerOrder(models.Model):
    ownerPDFlist=models.ForeignKey(ownerPDFlist, on_delete=models.CASCADE)
    Slno=models.IntegerField()
    name=models.CharField(max_length=300)
    price = models.IntegerField()
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.Slno} - {self.name} - {self.price} - {self.completed}"

    class Meta:
        verbose_name_plural="OwnerOrder"



class CredentialList(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "CredentialList"
        
    
class StudentCredentials(models.Model):
    CredentialList=models.ForeignKey(CredentialList, on_delete=models.CASCADE)
    regno = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.regno
    
    class Meta:
        verbose_name_plural = "StudentCredentials"



class OwnerCredentials(models.Model):
    CredentialList=models.ForeignKey(CredentialList, on_delete=models.CASCADE)
    regno = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.regno
    
    class Meta:
        verbose_name_plural = "OwnerCredentials"