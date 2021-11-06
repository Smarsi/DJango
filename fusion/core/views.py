from django.views.generic import TemplateView

from .models import Servico, Funcionario, Features

class IndexView(TemplateView):
    template_name = 'index.html' #Template view só precisa que indiquemos o nome do template que será usado para funcionar.

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        features = Features.objects.all()
        features_sort = [features[i::2] for i in range(2)]

        print(f'Esquerda {features_sort[0]}')
        print(f'Direita {features_sort[1]}')

        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features_l'] = features_sort[0]
        context['features_r'] = features_sort[1]
        return context