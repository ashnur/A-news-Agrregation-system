# Generated by Django 2.0.7 on 2018-07-25 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='International',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='National',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
    ]
