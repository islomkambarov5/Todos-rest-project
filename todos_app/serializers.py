from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from .models import Todos


class TodosSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Todos
        fields = ('user', 'title', 'description', 'is_completed')
