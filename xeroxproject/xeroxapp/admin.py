from django.contrib import admin
from .models import ownerPDFlist, PDF, studentPDFlist, studentPDF, CredentialList, Credentials
# Register your models here.
admin.site.register(ownerPDFlist)
admin.site.register(PDF)
admin.site.register(studentPDFlist)
admin.site.register(studentPDF)
admin.site.register(CredentialList)
admin.site.register(Credentials)
