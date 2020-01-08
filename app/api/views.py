from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from api import serializers
from api.utils import skill_cleaner, skill_compare


class TestProfileView(views.APIView):
    serializer_class = serializers.SkillsSerializer

    def get(self, request):
        return Response({"message": "Add your profile skills separated by comma"})

    def post(self, request):
        serializer = serializers.SkillsSerializer(data=request.data)

        if serializer.is_valid():

            skillset = request.data['skills']
            skills = skill_cleaner(skillset)
            results_dictionary, missing_dictionary = skill_compare(skills)

            return Response({"found": results_dictionary, "missing": missing_dictionary})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
