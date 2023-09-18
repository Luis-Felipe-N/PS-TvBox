import subprocess
from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import FormView
from desafios.models.Submissao import Submissao
from desafios.forms import SubmissaoForm
from desafios.models import Desafio

from cadastro.models import Pessoa
class SubmissaoCreateView(FormView):
    model = Submissao
    form_class = SubmissaoForm
    template_name = 'submissaoForm.html'
    success_url = '/codejunior/resultado/'

    def executarCodigo(self, codigo):
        try:
            resultadoBytes = subprocess.check_output(['python', '-c', codigo], stderr=subprocess.STDOUT, timeout=10)
            resultadoStr = resultadoBytes.decode('utf-8')
            print(f'Resultado: {resultadoStr}')
            return resultadoStr
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
        except subprocess.TimeoutExpired:
            return "Tempo limite excedido."
        
    def post(self, request, *args, **kwargs):

        problema = Desafio.objects.get(id=self.request.POST['problema'])
        print(f'Problema: {problema}')
        codigo = self.request.POST['codigo']
        resultadoUsuario = self.executarCodigo(codigo)
        submissao = Submissao()
    
        submissao.pessoa = Pessoa.objects.get(user=self.request.user)
        submissao.codigo = codigo
        submissao.problema = problema
    
        if resultadoUsuario.strip() == problema.solucao.strip():
            submissao.resultado = "Passou"
        else:
            submissao.resultado = "Falhou"

        submissao.save()
        
        return super().post(request, *args, **kwargs)