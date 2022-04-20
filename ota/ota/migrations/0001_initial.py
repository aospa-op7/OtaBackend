# Generated by Django 4.0.4 on 2022-04-20 12:35

from django.db import migrations, models
import django.db.models.deletion
import markdownfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code_name', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OtaPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('changelog', markdownfield.models.MarkdownField(rendered_field='changelog_rendered')),
                ('changelog_rendered', markdownfield.models.RenderedMarkdownField()),
                ('download_url', models.URLField()),
                ('version', models.CharField(max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ota_packages', to='ota.device')),
            ],
        ),
    ]
