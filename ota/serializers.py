from rest_framework import serializers

from ota.models import Device, OtaPackage



class OtaPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtaPackage
        fields = (
            'date_added',
            'changelog',
            'download_url',
            'version',
            'hash',
        )

class DeviceSerializer(serializers.ModelSerializer):
    ota_packages = OtaPackageSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = (
            'name',
            'code_name',
            'date_added',
            'ota_packages'
        )