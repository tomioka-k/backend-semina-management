from rest_framework import viewsets
from rest_framework import permissions
from .permission import IsAdminUserOrAuthenticatedReadOnly
from .models import Seminar
from .serializers import SeminarSerializers


class SeminarViewSet(viewsets.ModelViewSet):
    queryset = Seminar.objects.all()
    permissions = (IsAdminUserOrAuthenticatedReadOnly, )
    serializer_class = SeminarSerializers

    def perform_create(self, serializer):
        creater = self.request.user
        serializer.save(creater=creater)
