from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    class Meta:
        model = Person
        fields = "__all__"   