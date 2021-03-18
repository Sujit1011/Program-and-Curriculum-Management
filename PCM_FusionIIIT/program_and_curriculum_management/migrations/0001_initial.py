# Generated by Django 3.1.7 on 2021-03-17 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('batch_year', models.IntegerField(default=2021)),
                ('version', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_no', models.IntegerField()),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program_and_curriculum_management.curriculum')),
            ],
        ),
        migrations.AddField(
            model_name='curriculum',
            name='programme_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program_and_curriculum_management.programme'),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('credits', models.IntegerField(default=0)),
                ('contact_hours_Lecture', models.IntegerField(default=0)),
                ('contact_hours_Tutorial', models.IntegerField(default=0)),
                ('contact_hours_Lab', models.IntegerField(default=0)),
                ('syllabus', models.CharField(max_length=5000)),
                ('evaluation_schema', models.CharField(max_length=1000)),
                ('ref_books', models.CharField(max_length=2000)),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program_and_curriculum_management.semester')),
            ],
        ),
    ]