# Generated by Django 5.0.8 on 2024-08-18 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_course_course_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='teacher_name',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications_as_teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='for_students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'user_type': 'student'}, related_name='notifications_as_student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
