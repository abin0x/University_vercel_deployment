# Generated by Django 5.0.8 on 2024-08-29 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_researchpaper_img_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CRNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('course_code', models.CharField(blank=True, max_length=20, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='cr_notifications/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.course')),
                ('created_by', models.ForeignKey(blank=True, limit_choices_to={'user_type': 'student'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cr_notifications_created', to=settings.AUTH_USER_MODEL)),
                ('for_students', models.ManyToManyField(blank=True, limit_choices_to={'user_type': 'student'}, related_name='cr_notifications_as_student', to=settings.AUTH_USER_MODEL)),
                ('for_teachers', models.ManyToManyField(blank=True, limit_choices_to={'user_type': 'teacher'}, related_name='cr_notifications_as_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]