from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser,Media,Tenant
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer ,MediaSerializer,TenantSerializer

class UserViewSet(viewsets.ModelViewSet):
    q=CustomUser.objects.all()
    serializer=UserSerializer
    permission=[IsAuthenticated]

    def get_queryset(self):
        return self.q.filter(tenant=self.request.user.tenant)


class MediaViewSet(viewsets.ModelViewSet):
    q = Media.objects.all()
    serializer = MediaSerializer
    permission = [IsAuthenticated]

    def get_queryset(self):
        return self.q.filter(tenant=self.request.user.tenant)

    def perform_create(self,serializer):
        serializer.save(tenant=self.request.user.tenant)


class TenantViewSet(viewsets.ModelViewSet):
    q = Tenant.objects.all()
    serializer = TenantSerializer

    @action(details=True,method=['get'])
    def users(self, request,pk=None):
        tenant=self.get_object()
        users=CustomUser.objects.filter(tenant=tenant)
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)