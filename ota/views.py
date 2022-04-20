
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework import viewsets, permissions
from ota import serializers
from ota.custom_permissions import ReadOnly

from ota.serializers import DeviceSerializer, OtaPackageSerializer
from ota.models import Device, OtaPackage

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Device CRUD
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAdminUser | ReadOnly]

    @action(detail=True, methods=['get'])
    def ota(self, request, pk=None):
        """
        Gets all OTA packages for a given device
        """
        device = Device.objects.get(code_name=pk)
        serializer = OtaPackageSerializer(
            device.ota_packages, many=True, context={"request": request}
        )
        return Response(serializer.data)