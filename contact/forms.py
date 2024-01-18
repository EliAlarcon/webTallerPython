from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(label="Your name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':"Your name..."}
    ))
    email= forms.EmailField(label="Your email", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':"Your email..."}))
    phone= forms.CharField(label="Your phone", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':"Your phone..."}))
    message= forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows':4, 'placeholder':"Your message..."}
    ), min_length=10)