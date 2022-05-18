from rest_framework import serializers

from .models import Banco

class BancoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banco
        fields = ['CODIGO', 'NOME', 'ENDERECO']
