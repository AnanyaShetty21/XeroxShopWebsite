from django import forms

class AddPDF(forms.Form):
	Slno = forms.IntegerField(label = "Sl no.")
	name = forms.CharField(label = "Name", max_length = 300)
	price = forms.IntegerField(label = "Price")