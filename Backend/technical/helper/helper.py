from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import serializers, status
from ..models import Tokens


@api_view(["POST"])
@permission_classes([AllowAny])
def check_token(request):
    pass

