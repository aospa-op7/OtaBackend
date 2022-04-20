from django.db import models
from importlib_metadata import version
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

class Device(models.Model):
    name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

class OtaPackage(models.Model):
    device = models.ForeignKey(
        Device, related_name="ota_packages", on_delete=models.CASCADE
    )
    date_added = models.DateTimeField(auto_now_add=True)
    changelog = MarkdownField(rendered_field='changelog_rendered', validator=VALIDATOR_STANDARD)
    changelog_rendered = RenderedMarkdownField()
    download_url = models.URLField()
    version = models.CharField(max_length=255)
    hash = models.TextField()

    class Meta:
        ordering = ("date_added",)
    
    def __str__(self) -> str:
        return f"{self.device.name} - {self.version}"
