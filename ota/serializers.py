from rest_framework import serializers

from ota.models import Device, OtaPackage

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    ota_packages = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='ota_packages'
    )
    class Meta:
        model = Device
        fields = (
            'name',
            'code_name',
            'date_added',
            'ota_packages'
        )
    
class OtaPackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OtaPackage
        fields = (
            'device',
            'date_added',
            'changelog',
            'download_url',
            'version',
            'hash',
        )