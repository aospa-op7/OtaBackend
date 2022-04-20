from django.contrib import admin

from ota.models import Device, OtaPackage

admin.site.register(Device)
admin.site.register(OtaPackage)