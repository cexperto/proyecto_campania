from django.core import mail
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status

from contact.models import Contac

from .serializer import AllContactSerializer
from users.models import Users
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from users.utils import render_to_pdf
from contact.utils import send_email_contact


class ContactRegister(generics.ListAPIView):
    serializer_class = AllContactSerializer
    def get_queryset(self):
        try:
            contact = Contac.objects.filter(user_fk_id=self.request.user)
            return contact
        except TypeError:
            return print('Dont have access')
    
    def post(self, request, format=None):
        serializer = AllContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = 'sac@simonizco.com'
            correo = request.data['correo']
            nombre = request.data['nombre']
            telefono = request.data['telefono']
            mensaje = request.data['mensaje']
            send_email_contact(email, nombre, correo, mensaje, telefono)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ExportContactReport(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            if request.auth:
                contact = Contac.objects.all()
                data = {
                    'count': contact.count(),
                    'contact': contact
                }
                pdf = render_to_pdf('contact/report.html', data)
                return HttpResponse(pdf, content_type='application/pdf')
        except AssertionError:
            return
