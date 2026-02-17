from django import forms
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Libro, Autor
from .forms import LibroForm, AutorForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('libros:autores')
    template_name="libros/crear_autor.html"

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('libros:lista')
    template_name="libros/crear_libro.html"
    

class InicioPageView(TemplateView):
    template_name="libros/inicio.html"

class AutoresPageView(ListView):
    model = Autor
    template_name="libros/autores.html"
    context_object_name = "autores"
    def post(request,self, *args, **kwargs):
            autores = Autor.objects.all()
            return render(request,"libros/autores.html", self.template_name ,{"autores":autores})
    

class LibrosPageView(ListView):
    model = Libro
    template_name="libros/libros.html"
    context_object_name = "libros"

    def post(request,self, *args, **kwargs):
            libros = Libro.objects.all()
            return render(request,"libros/libros.html", self.template_name ,{"libros":libros})

class AutorUpdate(UpdateView):
        model = Autor
        fields = ['nombre','nacionalidad','foto','descripcion']
        template_name_suffix = '_update_form'
        success_url = reverse_lazy('libros:autores')
        template_name = "libros/autor_update_form.html"
        
class LibrosUpdate(UpdateView):
        model = Libro
        fields = ['titulo','autor','fecha_publicacion','disponible','descripcion']
        template_name_suffix = '_update_form'
        success_url = reverse_lazy('libros:lista')
        template_name = "libros/libro_update_form.html"

class LibrosDelete(DeleteView):
      model =Libro
      template_name = 'libros/libro_confirm_delete.html'
      success_url = reverse_lazy('libros:lista')

class AutoresDelete(DeleteView):
      model =Autor
      template_name = 'libros/autor_confirm_delete.html'
      success_url = reverse_lazy('libros:autores')

class AutorDetail(DetailView):
      model=Autor
      template_name ="libros/autor.html"
      def get_object(self):
            return get_object_or_404(Autor,pk=self.kwargs['pk'])
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['obras'] = Libro.objects.filter(autor=self.object)
            return context
      
class LibroDetail(DetailView):
      model=Autor
      template_name ="libros/libro.html"
      def get_object(self):
            return get_object_or_404(Libro,pk=self.kwargs['pk'])
        