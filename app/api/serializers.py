from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """For request.user logic in Vue.js frontend"""

    class Meta:
        model = User
        fields = ["email"]


class SkillsSerializer(serializers.Serializer):
    """For evaluate skillset view"""
    skills = serializers.CharField(max_length=1000)
