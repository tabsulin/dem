from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def GetData(request):
    a = {'a':'akhil'}
    return Response(a)