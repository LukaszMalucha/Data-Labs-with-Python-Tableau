from rest_framework import serializers

from core.models import User, Property


class UserSerializer(serializers.ModelSerializer):
    """For request.user logic in Vue.js frontend"""

    class Meta:
        model = User
        fields = ["email"]


class SkillsSerializer(serializers.Serializer):
    skills = serializers.CharField(max_length=1000)


class PropertySerializer(serializers.ModelSerializer):
    # city = serializers.CharField(max_length=1000)
    # area = serializers.CharField(max_length=1000)
    # property_type = serializers.CharField(max_length=1000)
    # bedrooms = serializers.IntegerField(min_value=1, max_value=15)
    # bathrooms = serializers.IntegerField(min_value=1, max_value=15)
    class Meta:
        model = Property
        fields = '__all__'