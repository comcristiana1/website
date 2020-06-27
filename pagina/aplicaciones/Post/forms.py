from django import forms
from .models import FormularioRecursos,Contactos,Edificadores

class O_PForm(forms.ModelForm):
    class Meta:
        model = FormularioRecursos
        fields = ['name_person','mail_persona','section_category','title','description']


        labels = {
            'name_person':'Ingresa tu Nombre',
            'mail_persona':'Ingresa tu email',
            'section_category':'¿Deseas una Oración o una Petición?',
            'title':'Titulo',
            'description':'Hablanos del tema',
        }
        widgets = {
            'name_person':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor',
                    'id':'nombre',
                }
            ),
            'title':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su tema',
                    'id':'titulo',
                }
            ),
            'section_category':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria',
                }
            ),                        
            'mail_persona':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo',
                    'id':'mail',
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la descripción',
                    'id':'descripcion',
                }
            )
        }




class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['name','surname','mail','message']



class EdificadoresForm(forms.ModelForm):
    class Meta:
        model = Edificadores
        fields = ['tipe','name','mail','description']
