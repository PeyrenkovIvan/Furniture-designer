# Generated by Django 2.2.12 on 2023-09-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenght', models.CharField(max_length=50)),
                ('width', models.CharField(max_length=50)),
                ('base', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
