from rest_framework import serializers

from .models import LittleG

class LittleGSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LittleG
        fields = ('problem', 'solution', 'datetime')