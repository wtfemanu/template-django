from attr import fields
from rest_framework.serializers import ModelSerializer

from core.models import editora


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = editora
        fields = '__all__'
        

