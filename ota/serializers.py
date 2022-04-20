from rest_framework import serializers

from ota.models import Device, OtaPackage

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = (
            'name',
            'code_name',
            'date_added'
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