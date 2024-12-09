# Generated by Django 5.1.3 on 2024-11-09 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadAnswerSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='answerKey',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ExaminationId', models.CharField(max_length=250)),
                ('Item', models.IntegerField()),
                ('Answer', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminationMain',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ExaminationId', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='examResult',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ExaminationId', models.CharField(max_length=250)),
                ('StudentIdNo', models.CharField(max_length=50)),
                ('Fullname', models.CharField(max_length=250)),
                ('Items', models.IntegerField()),
                ('Score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('StudentId', models.CharField(max_length=10)),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Middlename', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminationDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ExaminationMain', models.CharField(max_length=250)),
                ('StudentIdNo', models.CharField(max_length=50)),
                ('Fullname', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.student')),
            ],
        ),
    ]
