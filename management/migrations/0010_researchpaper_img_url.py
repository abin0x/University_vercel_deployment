# Generated by Django 5.0.8 on 2024-08-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_researchpaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchpaper',
            name='img_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]