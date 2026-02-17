import datetime
from django import forms
from .models import Autor, Libro
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','nacionalidad','foto','descripcion']
        labels={
            'nombre':"",
            'nacionalidad':"",
            'foto':'Foto',
            'descripcion':""
        }
        widgets={
            'nombre':forms.Textarea(attrs={'class':'form-control mt-3 mx-3','rows':1,'placeholder':'Nombre'}),
            'nacionalidad':forms.Textarea(attrs={'class':'form-control mt-3 mx-3','rows':1,'placeholder':'Nacionalidad'}),
            'foto':forms.ClearableFileInput(attrs={'class':"rounded mx-auto d-block form-control mt-3 mx-3"}),
            'descripcion':forms.Textarea(attrs={'class':'form-control mt-3','rows':5,'placeholder':'Descripcion'}),
        }

class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.IntegerField( 
            label="",
            min_value=1500,
            max_value=datetime.date.today().year,
            widget=forms.NumberInput(attrs={
                'class':'form-control mt-3',
                'placeholder':'Año'
            })
        )
    class Meta:
        model = Libro
        fields = ['titulo','autor','fecha_publicacion','disponible','descripcion']
        labels={
            'titulo':"",
            'autor':"Autor",
            'fecha_publicacion':'',
            'disponible':"Disponible",
            'descripcion':""
        }
        widgets={
            'titulo':forms.Textarea(attrs={'class':'form-control mt-3','rows':1,'placeholder':'Titulo'}),
            'autor':forms.Select(attrs={'class':'form-control mt-3','rows':1,'placeholder':'Autor'}),
            'disponible': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control mt-3','rows':5,'placeholder':'Descripcion'}),
        }