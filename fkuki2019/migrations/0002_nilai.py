# Generated by Django 3.2.7 on 2021-10-01 20:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('fkuki2019', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', tinymce.models.HTMLField(default='')),
            ],
        ),
    ]
