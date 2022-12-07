from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required


@login_required
def get_token(admin):
    access = AccessToken.for_user(admin)

    if Response(status=status.HTTP_200_OK):
        pass