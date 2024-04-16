from django.shortcuts import render,redirect
from django.views.generic.base import View
from users.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User

class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
      

        if form.is_valid():
            dados_form = form.data
          

            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

            redirect('index')
            

        return render(request, self.template_name, {'form' :form})
