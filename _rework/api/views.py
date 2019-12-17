from rest_framework import views, status, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views

from api import serializers
from api.utils import skill_cleaner, skill_compare


class CurrentUserApiView(views.APIView):
    """Get currently logged user"""
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)


class TestProfileView(views.APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SkillsSerializer

    def get(self, request):
        return Response({"message": "Add your profile skills separated by comma"})

    def post(self, request):
        serializer = serializers.SkillsSerializer(data=request.data)

        if serializer.is_valid():
            skillset = request.data['skills']
            try:
                skills = skill_cleaner(skillset)
                results_dictionary, missing_dictionary = skill_compare(skills)
            except:
                return Response({'message': "Invalid Request"},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response({"found": results_dictionary,
                             "missing": missing_dictionary})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstimatePropertyView(views.APIView):
    serializer_class = serializers.PropertySerializer

    def get(self, request):
        return Response({"message": "Specify the property details."})

    def post(self, request):
        serializer = serializers.PropertySerializer(data=request.data)

        if serializer.is_valid():
            property_data = str(request.data)
            return Response({"property": property_data})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
