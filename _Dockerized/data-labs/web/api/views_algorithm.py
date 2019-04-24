from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api import serializers
from daft_analytics.utils import price_regressor, cork_path, dublin_path, galway_path, limerick_path
from data_science.utils import skill_cleaner, skill_compare


class EstimatePropertyView(APIView):
    """Apply Property Value Estimator algorithm"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PropertySerializer

    def get(self, request):
        return Response({"message": "Specify estimated property features"})

    def post(self, request):
        serializer = serializers.PropertySerializer(data=request.data)

        if serializer.is_valid():
            city = request.POST.get('city')
            if city == "Cork":
                dataset = cork_path
            elif city == "Dublin":
                dataset = dublin_path
            elif city == "Galway":
                dataset = galway_path
            else:
                dataset = limerick_path
            area = request.POST.get('area')
            bedrooms = request.POST.get('bedrooms')
            bathrooms = request.POST.get('bathrooms')
            estimated_type = request.POST.get('property_type')
            if estimated_type == "House":
                property_type = 1
            else:
                property_type = 0
            try:
                estimators = price_regressor(dataset, area, property_type, bedrooms, bathrooms)
                estimators = sorted(estimators, key=int)
            except:
                return Response({'message': "{} area doesn't belong to {} city".format(area, city)},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": request.data,
                             "Estimated Property Value": "{} - {}".format(estimators[0], estimators[1])})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestProfileView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SkillsSerializer

    def get(self, request):
        return Response({"message": "Add your profile skills separated by comma"})

    def post(self, request):
        serializer = serializers.SkillsSerializer(data=request.data)

        if serializer.is_valid():
            skillset = request.POST.get('skills')
            try:
                skills = skill_cleaner(skillset)
                results_dictionary, missing_dictionary = skill_compare(skills)
            except:
                return Response({'message': "Invalid Request"},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response({"Found on % of Data Scientists Linkedin Profiles": results_dictionary,
                             "% of Data Scientists also listed": missing_dictionary})






        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
