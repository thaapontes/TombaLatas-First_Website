from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PerfilCao(models.Model):
    nome = models.CharField(max_length = 30, null = False)
    tipo = models.CharField(max_length=255, default = 'SOME STRING')
    endereco=models.CharField(max_length = 50, null=False)
    caracteristicas= models.CharField(max_length = 200, null = False)
    usuario = models.OneToOneField(User, related_name="perfil")

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()

class Convite(models.Model):
    solicitante = models.ForeignKey(PerfilCao, related_name='convites_feitos')
    convidado = models.ForeignKey(PerfilCao, related_name='convites_recebidos')
    