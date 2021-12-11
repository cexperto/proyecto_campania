from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import AllUserSerializer
from users.models import Users
from rest_framework import generics, status
from .serializer import AllUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .utils import render_to_pdf, send_email
from django.http import HttpResponse
import boto3

s3 = boto3.resource('s3')


def home(request):
    return HttpResponse("Welcome to the API!")

class UserRegisterList(APIView):
    # def get(self, request, format=None):
    #     users = Users.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AllUserSerializer(data=request.data)
        if serializer.is_valid():
            correo = request.data['correo']            
            # serializer.save()
            send_email(correo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilterUser(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = AllUserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['factura']


class ListUsers(generics.ListAPIView):
    serializer_class = AllUserSerializer

    def get_queryset(self):
        try:
            users = Users.objects.filter(user_fk_id=self.request.user)
            return users
        except TypeError:
            return print('Dont have access')


class ExportReport(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            if request.auth:
                users = Users.objects.all()
                data = {
                    'count': users.count(),
                    'users': users
                }
                pdf = render_to_pdf('users/report.html', data)
                return HttpResponse(pdf, content_type='application/pdf')
        except AssertionError:
            return
