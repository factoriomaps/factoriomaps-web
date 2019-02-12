from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer


class UserView(APIView):
    """
    User Creation
    """
    def get(self, request):
        """
        # TODO do this better
        :param request:
        :return:
        :rtype: Response
        """
        user = get_object_or_404(User, **request.query_params)
        return Response({'username': user.username, 'e-mail': user.email}, status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
