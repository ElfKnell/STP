from rest_framework import serializers
from .models import Section


class SectionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name_section', 'color', 'description', 'user')


class SectionDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Section
        fields = '__all__'
