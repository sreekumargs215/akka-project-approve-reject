# Generated by Django 2.1.8 on 2023-10-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planapp', '0003_profile_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]