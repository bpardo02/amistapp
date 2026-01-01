from django import forms
from .models import Noticia, Recuerdo

BASE = "w-full border-2 border-black px-3 py-2 font-terminal text-xl"

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': BASE}),
            'contenido': forms.Textarea(attrs={'class': BASE, 'rows': 4}),
        }

class RecuerdoForm(forms.ModelForm):
    class Meta:
        model = Recuerdo
        fields = ['titulo', 'descripcion', 'archivo']

class ResenaForm(forms.Form):
    nombre = forms.CharField()
    categoria = forms.CharField()
    puntaje = forms.IntegerField(min_value=1, max_value=5)
    comentario = forms.CharField(widget=forms.Textarea)
