# Generated by Django 3.0.6 on 2020-10-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portofolio',
            fields=[
                ('porto_id', models.AutoField(primary_key=True, serialize=False)),
                ('porto_project_name', models.CharField(max_length=100)),
                ('porto_project_desc', models.TextField()),
                ('porto_created_by', models.CharField(max_length=100)),
                ('porto_photo', models.ImageField(upload_to='msb/assets/images/portofolio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
