# Generated by Django 4.1.7 on 2023-04-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('details', models.TextField()),
                ('is_complete', models.BooleanField()),
                ('is_pinned', models.BooleanField()),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Attachments',
            fields=[
                ('attachments_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_app.task')),
            ],
        ),
    ]
