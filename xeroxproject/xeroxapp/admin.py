from django.contrib import admin
from .models import ownerPDFlist, PDF, studentPDFlist, studentPDF, OwnerOrder, CredentialList, StudentCredentials, OwnerCredentials
# Register your models here.
admin.site.register(ownerPDFlist)
admin.site.register(PDF)
admin.site.register(studentPDFlist)
admin.site.register(studentPDF)
admin.site.register(OwnerOrder)
admin.site.register(CredentialList)
admin.site.register(StudentCredentials)
admin.site.register(OwnerCredentials)