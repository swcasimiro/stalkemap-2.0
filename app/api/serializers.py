from rest_framework import serializers
from events.models import Events, ResponseEvent


class EventLocalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # заполняет автоматически поле user

    class Meta:
        model = Events
        fields = '__all__'


class EventGlobalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Events
        fields = '__all__'


class ResponseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseEvent
        fields = '__all__'
