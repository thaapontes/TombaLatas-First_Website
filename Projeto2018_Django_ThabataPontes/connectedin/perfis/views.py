from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import PerfilCao
from django.shortcuts import redirect
from perfis.forms import RegistrarAnimalForm
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'ONGTombaLatas.html')

def exibir(request, perfil_id):
    perfil = PerfilCao.objects.get(id=perfil_id)
    return render(request, 'perfil.html', { "perfil" : perfil })

def galeria(request):
    return render(request, 'galeria.html')

@login_required 
def registro(request):
    return render(request, 'registro.html', {'perfis':PerfilCao.objects.all(),'perfil_logado' : get_perfil_logado(request)})

def convidar(request, perfil_id):
    perfil_a_convidar = PerfilCao.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('registro');

def get_perfil_logado(request):
    return request.user

class RegistrarAnimalView(View):

    template_name = 'registro.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        formAnimal = RegistrarAnimalForm(request.POST)

        if form.is_valid():
            dados_formAnimal = formAnimal.data

            perfil = PerfilCao.objects.create(nome=dados_formAnimal['nome'],
                            tipo = dados_formAnimal['tipo'],
                            endereco = dados_formAnimal['endereco'],
                            caracteristicas = dados_formAnimal['caracteristicas'],
                            usuario = usuario)
            perfil.save()
            return redirect('registro')

        return render(request, self.template_name, {'form' :form})