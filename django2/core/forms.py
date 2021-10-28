from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100,  min_length=3)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject = 'E-mail enviado pelo sistema django2',
            body = conteudo,
            from_email = 'contato@seu-dominio.com.br',
            to = ['contato@seu-dominio.com.br',],
            headers = {'Reply-To': email}
        )

        mail.send()

#Para formulários que terão acesso para realizar operações no Banco De Dados usamos os ModelForm

class ProdutoModelForm(forms.ModelForm): #Podemos diferenciar o Form do Model Form pelo item herdado na classe.
    class Meta: #Aqui temos os MetaDados dessa classe. Nesse caso , estamos passando Meta Dados do fomulário de Produtos
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'image']
