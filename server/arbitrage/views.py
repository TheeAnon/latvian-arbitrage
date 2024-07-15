from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ArbitrageOpportunity
from .serializers import ArbitrageOpportunitySerializer

# List all arbitrages
@api_view(['GET'])
def get_arbitrages(request):
    arbitrages = ArbitrageOpportunity.objects.all()
    serializer = ArbitrageOpportunitySerializer(arbitrages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_arbitrage(request):
    competitors = request.data.get('competitors')
    site_one_name = request.data.get('site_one_name')
    site_two_name = request.data.get('site_two_name')
    market = request.data.get('market')

    try:
        existing_entry = ArbitrageOpportunity.objects.get(
            competitors=competitors,
            site_one_name=site_one_name,
            site_two_name=site_two_name,
            market=market
        )
        serializer = ArbitrageOpportunitySerializer(existing_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ArbitrageOpportunity.DoesNotExist:
        serializer = ArbitrageOpportunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
