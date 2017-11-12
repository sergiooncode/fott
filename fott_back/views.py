from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    now = datetime.datetime.now()
    return Response({'time': now})
