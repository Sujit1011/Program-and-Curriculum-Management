# Generated by Django 3.1.7 on 2021-03-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program_and_curriculum_management', '0002_auto_20210318_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='version',
            field=models.CharField(max_length=50),
        ),
    ]
