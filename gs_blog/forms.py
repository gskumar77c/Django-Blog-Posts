from django import forms


class GeeksForm(forms.Form): 
    title = forms.CharField() 
    description = forms.CharField()


class Myform(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
