from django.contrib import admin
from .models import ownerPDFlist, PDF, CredentialList, Credentials
# Register your models here.
admin.site.register(ownerPDFlist)
admin.site.register(PDF)
admin.site.register(CredentialList)
admin.site.register(Credentials)