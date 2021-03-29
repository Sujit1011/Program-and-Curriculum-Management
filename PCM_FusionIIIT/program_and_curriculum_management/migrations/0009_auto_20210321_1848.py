# Generated by Django 3.1.7 on 2021-03-21 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program_and_curriculum_management', '0008_semester_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program_and_curriculum_management.courses'),
        ),
    ]