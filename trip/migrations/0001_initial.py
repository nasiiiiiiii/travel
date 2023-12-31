# Generated by Django 4.2.5 on 2023-10-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('img', models.ImageField(upload_to='my_pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='my_pics')),
            ],
        ),
    ]
