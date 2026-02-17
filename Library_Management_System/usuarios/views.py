from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Registro
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator



class UsuarioMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super(UsuarioMixin, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name = 'dispatch')
class RegistroView(UsuarioMixin,CreateView):
    form_class = Registro
    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    template_name = 'usuarios/registro.html'
    def get_form(self, form_class = None):
        form =super(RegistroView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form
