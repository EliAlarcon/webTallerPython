from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    # print(f'Tipo de petición: {request.method}')
    #Instanciamos la clase que contiene el formulario
    contact_form=ContactForm() # Formulario vacio
    if request.method == 'POST':
        contact_form=ContactForm(data=request.POST) # Se rellena el formulario con los datos ingresados
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            phone=request.POST.get('phone','')
            message=request.POST.get('message','')
            # Estructura del correo
            email=EmailMessage(
                "SAN JORGE ECO-LODGES: Mensaje de contacto nuevo",
                f"Hola, {name} <{email}>:\n\nEscribió:\n{message}.\n\nContacto: {phone}",
                f"{email}",
                ["magic.birding@gmail.com"],
                reply_to=[email],
            )
            # Enviar el correo
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

            return redirect(reverse('contact')+"?ok")
    return render(request, "contact/contact.html", {'contact_form': contact_form})