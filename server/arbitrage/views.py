from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ArbitrageOpportunity
from .serializers import ArbitrageOpportunitySerializer

# List all arbitrages
@api_view(['GET'])
def get_all_arbitrages(request):
    arbitrages = ArbitrageOpportunity.objects.all()
    serializer = ArbitrageOpportunitySerializer(arbitrages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# List all active arbitrages
@api_view(['GET'])
def get_active_arbitrages(request):
    arbitrages = ArbitrageOpportunity.objects.filter(active=True)
    serializer = ArbitrageOpportunitySerializer(arbitrages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# List all inactive arbitrages
@api_view(['GET'])
def get_inactive_arbitrages(request):
    arbitrages = ArbitrageOpportunity.objects.filter(active=False)
    serializer = ArbitrageOpportunitySerializer(arbitrages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)