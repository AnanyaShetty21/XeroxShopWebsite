from django import forms

class AddPDF(forms.Form):
	Slno = forms.IntegerField(label = "slno")
	name = forms.CharField(label = "name", max_length = 300)
	price = forms.IntegerField(label = "price")