# Generated by Django 3.0.6 on 2020-07-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200703_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='uf',
            field=models.CharField(max_length=100),
        ),
    ]