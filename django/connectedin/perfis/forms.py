from django import forms
from perfis.models import PerfilCao

class RegistrarAnimalForm(forms.Form):

    nome = forms.CharField(required=True)
    tipo = forms.ChoiceField(required=True)
    endereco = forms.CharField(required=True)
    caracteristicas = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarAnimalForm, self).is_valid():
            self.adiciona_erro('Por favor verifique os dados informados')
            valid = False

        animal_exists = PerfilCao.objects.filter(username=self.data['nome']).exists()

        if animal_exists:
            self.adiciona_erro('Animal ja existente')
            valid = False

        return valid
    def adiciona_erro(self, message):
        erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)